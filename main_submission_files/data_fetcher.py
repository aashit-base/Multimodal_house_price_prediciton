import math
import requests
import pandas as pd
from PIL import Image
from io import BytesIO
from pathlib import Path

ZOOM = 18
IMAGE_SIZE = 299 
# for inception model
BASE_URL = (
    "https://server.arcgisonline.com/ArcGIS/rest/services/"
    "World_Imagery/MapServer/tile"
)

# As arcGIS gets images by tiles which have different coordinates than longitude and latitude.
def latlon_to_tile(lat, lon, zoom):
    lat = math.radians(lat)
    n = 2 ** zoom
    x = int((lon + 180)/360 * n)
    y = int((1 - math.log(math.tan(lat)+1 / math.cos(lat))/math.pi)/ 2 * n)
    return x, y

def fetch_images(csv_path, out_dir):
    df = pd.read_csv(csv_path)
    out_dir.mkdir(parents=True, exist_ok=True)

    for idx, row in df.iterrows():
        img_id = row["id"] if "id" in df.columns else idx
        img_path = out_dir / f"{img_id}.png"

        if img_path.exists():
            continue

        x, y = latlon_to_tile(row["lat"], row["long"], ZOOM)
        url = f"{BASE_URL}/{ZOOM}/{y}/{x}" 
        # format for searching

        img = Image.open(BytesIO(requests.get(url).content)).convert("RGB")
        img = img.resize((IMAGE_SIZE, IMAGE_SIZE))
        img.save(img_path)


BASE = Path("/content/drive/MyDrive") #destination of images
fetch_images(csv_path=BASE / "train_preprocessed.csv", out_dir=BASE / "satellite_images/train",)
fetch_images(csv_path=BASE / "test_preprocessed.csv",out_dir=BASE / "satellite_images/test",)
