from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import json
from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', views.first, name='first'),
    path('first/', views.first, name='first'),
    path('login/', views.login, name='login'),
    path('chart/', views.chart, name='chart'),
    path('index/', views.index, name='index'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tongue_disease.urls')),
]


MODEL = tf.keras.models.load_model(r"./saved_model/1", compile=False)
CLASS_NAMES = [
    'hairytonguedataset',
    'healthytonguedataset',
    'leokoplakiatonguedataset',
    'oralcancerdataset',
    'orallichensdataset',
    'oralthrushdataset'
]

disease_dictionary = {}
with open(r"./saved_model/details.json", 'r') as source_file:
    CONDITION_DATA = json.load(source_file)
    disease_con = CONDITION_DATA.get('disease_condition', [])

def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data))
    image = image.resize((256, 256)).convert("RGB")
    return np.array(image)

def first(request):
    return render(request, "first.html")

def login(request):
    return render(request, "login.html")

def chart(request):
    return render(request, "chart.html")

def index(request):
    if request.method == "POST":
        image = request.FILES.get('imagefile')
        if not image:
            return render(request, "index.html", {"error": "No image provided."})

        image = Image.open(image)
        with BytesIO() as buf:
            image.save(buf, 'jpeg')
            image = buf.getvalue()

        global disease_dictionary
        image = read_file_as_image(image)
        img_batch = np.expand_dims(image, 0)

        predictions = MODEL.predict(img_batch)
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])

        for i in disease_con:
            if i['predicted_class'] == predicted_class:
                disease_dictionary = {
                    "Disease": i['condition'],
                    "Description": i['description'],
                    "Symptoms": i['symptoms'],
                    "Causes": i['causes'],
                    "Treatments": i['treatment']
                }
                break

        return render(request, "index.html", {
            "prediction": disease_dictionary.get("Disease"),
            "description": disease_dictionary.get("Description"),
            "symptoms": disease_dictionary.get("Symptoms"),
            "causes": disease_dictionary.get("Causes"),
            "treatment": disease_dictionary.get("Treatments"),
            "confidence": confidence
        })

    return render(request, "index.html")
