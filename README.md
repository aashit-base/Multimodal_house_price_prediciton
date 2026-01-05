readme_md: |
# MULTIMODAL HOUSE PRICE PREDICTION

This repository contains the code and files required to preprocess data, train a multimodal model (tabular + satellite images), and generate house price predictions. 
It also includes the some files produced during training and prediction by myself as well. 
Furthermore , the main submission file which were strictly necessary are put into main_submission_files.

---

## Repository Structure

```text
MULTIMODAL_HOUSE_PRICE_PREDICTION/
│
├── DATA/
│ └── train_dataset.csv
| └── test_dataset.csv
│
├── main_submission_files/
│ └── 24322002_final.csv
│ └── data_fetcher.py
│ └── preprocessing.ipynb
│ └── model_training.ipynb
│ └── 24322002_report.pdf
│
│
├── media/
│ ├── compare.png
│ ├── grad_cam_high.png
│ ├── grad_cam_low.png
│ ├── high_image.png
│ ├── low_image.png
│ └── train_loss.png
│
├── EDA_profile.html
├── final_fusion_model.pt
├── tabular_scaler.pkl
├── train_preprocessed.csv
├── test_preprocessed.csv
│
├── requirements.txt
└── README.md

```
---

## Setup Instructions

1. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate        # Linux / Mac
venv\Scripts\activate           # Windows

```
2. Install required dependencies

```bash
pip install -r requirements.txt

```
> Tested with Python 3.x

---

## How to Run the Code

1. Download satellite images
```bash
python data_fetcher.py
```

The file has BASE var which stores the path where the images are to be stored, I originally 
downloaded all the images to my drive through google colab. One can change it.

2. Preprocess the data

Open and run all cells in: **preprocessing.ipynb** 
*(I have added instructions as comments and divided into sections)*

This will lead to creation of two preprocessed_test and train datasets which will be used for prediction
and training of the model. Also , an **EDA_profile.html** file will be created which will give 
an overview of Data.

3. Train the model

Open and run all cells in: **model_training.ipynb**

There are multiple models in this file (from linear to complex neural networks).
I have also included the performances of these models in **compare.png** in **media** folder.

You can follow the headings and comments as guides , few cells are only to be run once while 
others can be run as many times as one wishes. 

I have also made sections to navigate it (**final_model** is the main training model)
It also includes the process of predicting and making of submission file.
An image of the final_model training loss is also available in media folder.


*Mainly 5 files will be created through this.*
- final_fusion_model.pt
- tabular_scaler.pkl
- train_preprocessed.csv
- test_preprocessed.csv
- 24322002_final.csv


The final file is the prediction file.

*2 more files will also form which are used to store image features generated from CNN.*
*This is done to speed up the process and do training quickly.*

4. Generate predictions
Final predictions are saved as: **main_submission_files/24322002_final.csv**
These are the main predictions saved in format of `id, predicted_price`.