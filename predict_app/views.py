from django.shortcuts import render, redirect
from django.http import HttpResponse

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import joblib

from predict_app.models import CropData
import datetime

# Create your views here.
def index(request):
    return HttpResponse(r'''
    <html>
        <head><title>Home | Crop Prediction</title></head>
        <body>
            <h2>Welcome to Project - Crop Prediction</h2>
        </body>
    </html>
    ''')
    # return render(request, 'index.html')

def predict(request):
    if request.method != 'POST':
        return render(request, 'index.html')

    if request.method == 'POST':
        df = pd.read_csv("static/cp.csv")

        x = df.drop(columns=['label'], axis=1)
        y = df['label']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

        log_reg = LogisticRegression()
        log_reg.fit(x_train, y_train)
        
        with open('static/crop_prediction_model', 'wb') as f:
            pickle.dump(log_reg, f)
        
        N = int(request.POST['N'])
        P = int(request.POST['P'])
        K = int(request.POST['K'])
        temperature = float(request.POST['temperature'])
        humidity = float(request.POST['humidity'])
        ph = float(request.POST['ph'])
        rainfall = float(request.POST['rainfall'])

        model = joblib.load("static/crop_prediction_model")

        predict_value = model.predict([[N, P, K, temperature, humidity, ph, rainfall]])
        predict_value = str(predict_value[0])
        data = {'prediction':predict_value}

        entry = CropData(N=N, P=P, K=K, temperature=temperature, humidity=humidity, ph=ph, rainfall=rainfall, prediction=predict_value, date=datetime.datetime.now())
        entry.save()

        return render(request, 'prediction.html', data)

def report(request):
    records = CropData.objects.all()
    data = {'data':records}
    return render(request, 'report.html', data)