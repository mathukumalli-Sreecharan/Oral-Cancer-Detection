# Oral Cancer Detection

A Flask-based deep learning web application designed to detect oral diseases from uploaded tongue images and provide disease information, symptoms, causes, and treatment guidance.

## Overview

This project uses a TensorFlow/Keras model to classify oral conditions from images. The web application allows users to upload an image, process it through the trained AI model, and view the predicted disease with a supporting description.

## Problem Statement

Early detection is crucial for many oral diseases, including oral cancer. Many patients do not have easy access to clinical screening tools, and a simple image-based diagnostic support system can help identify suspicious conditions for further medical evaluation.

## Objectives

- Detect oral diseases from uploaded images
- Provide a user-friendly interface for image classification
- Display predicted disease details and treatment information
- Support educational and prototype-level medical diagnosis assistance

## Features

- Image upload functionality
- AI-based disease prediction
- Display of disease name and description
- Symptom, cause, and treatment details
- Responsive HTML/CSS front-end
- Flask backend for model inference

## Tech Stack

- Python
- Flask
- TensorFlow / Keras
- NumPy
- Pillow
- HTML
- CSS
- JavaScript

## Project Structure

```text
Oral Cancer Detection/
├── README.md
├── .gitignore
├── generate_word_docx.py
├── generate_workflow_doc.py
├── Project_Workflow_Oral_Cancer_Detection.docx
├── Code/
│   ├── app.py
│   ├── api/
│   │   └── requirements.txt
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   ├── templates/
│   │   ├── index.html
│   │   ├── first.html
│   │   ├── login.html
│   │   └── chart.html
│   ├── saved_model/
│   │   ├── details.json
│   │   └── 1/
│   └── models/
│       ├── model.h5
│       ├── model.json
│       └── 2/
│           └── ...
├── training/
│   └── trainingModel.ipynb
├── test images/
└── .idea/
```

## Prerequisites

Before running the project, ensure the following are installed:

- Python 3.9 or above
- pip
- Virtual environment support
- Web browser

## Setup Instructions

Open PowerShell and run these commands from the project root:

```powershell
cd "d:\B.Tech\Oral Cancer Detection"
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r .\Code\api\requirements.txt
```

If `python` is not recognized, use:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r .\Code\api\requirements.txt
```

## Run the Project

Start the Flask application:

```powershell
cd "d:\B.Tech\Oral Cancer Detection\Code"
python app.py
```

or:

```powershell
cd "d:\B.Tech\Oral Cancer Detection\Code"
py app.py
```

Then open the browser and visit:

```text
http://127.0.0.1:5000/
```

## How It Works

1. The user uploads an image.
2. The application preprocesses the image.
3. The trained TensorFlow model predicts the disease class.
4. The result is displayed along with disease information.
5. The system provides details such as symptoms, causes, and treatment suggestions.

## Model Details

The project includes trained model assets stored in:

- `Code/saved_model/`
- `Code/models/`

The model predicts categories such as:

- hairytonguedataset
- healthytonguedataset
- leokoplakiatonguedataset
- oralcancerdataset
- orallichensdataset
- oralthrushdataset

## Usage Notes

- This project is intended for academic, learning, and demo purposes.
- It is not a substitute for professional medical diagnosis.
- The model depends on local files present in the project directory.
- If the application is run from another location, ensure the relative paths in `Code/app.py` still resolve correctly.

## Future Improvements

- Improve model accuracy with more diverse training data
- Add data augmentation and better preprocessing
- Enhance the front-end design
- Add patient history tracking and reports
- Deploy the app to a cloud platform
- Add a doctor dashboard or admin panel

## Acknowledgements

This project was developed as an oral disease detection system using Python, Flask, and deep learning techniques. It is suitable for educational demonstration and research-oriented use.
