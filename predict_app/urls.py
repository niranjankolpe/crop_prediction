from django.contrib import admin
from django.urls import path
from predict_app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('home', index, name='home'),
    path('predict', predict, name='predict'),
    path('report', report, name='report')
]
