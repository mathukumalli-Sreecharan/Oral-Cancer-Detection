# Oral Cancer Detection

This project is a Flask-based web application that classifies oral health conditions from uploaded tongue images using a TensorFlow deep learning model.

## Project overview

- Upload an image through the web interface
- Classify the image using the trained model
- Display the predicted condition and its description, symptoms, causes, and treatment guidance

## Folder structure

- `Code/app.py` — Flask application entry point
- `Code/templates/` — HTML pages
- `Code/static/` — CSS and JavaScript assets
- `Code/saved_model/` — trained model files
- `Code/api/requirements.txt` — Python dependencies

## Prerequisites

- Python 3.9 recommended
- Windows PowerShell or any terminal

## Setup

```powershell
cd "d:\B.Tech\Oral Cancer Detection"
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r .\Code\api\requirements.txt
```

## Run the application

```powershell
cd "d:\B.Tech\Oral Cancer Detection\Code"
python app.py
```

Then open the app in your browser:

```text
http://127.0.0.1:5000/
```

If `python` is not recognized, use:

```powershell
py app.py
```

## Git commands to upload to GitHub

```bash
git init
git branch -M main
git add .
git commit -m "Initial commit"
git remote add origin <your-github-repo-url>
git push -u origin main
```

If you already created a GitHub repository and want to connect to it:

```bash
git remote set-url origin <your-github-repo-url>
git push -u origin main
```

## Notes

- The model files are included under the project folder and are required for prediction.
- The project is intended for local development and demonstration purposes.
