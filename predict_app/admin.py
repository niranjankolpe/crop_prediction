from django.contrib import admin

# Register your models here.
from predict_app.models import CropData

admin.site.register(CropData)