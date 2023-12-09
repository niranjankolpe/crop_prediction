from django.db import models
import datetime

# Create your models here.
class CropData(models.Model):
    id = models.AutoField(primary_key=True)
    N = models.IntegerField(default=0)
    P = models.IntegerField(default=0)
    K = models.IntegerField(default=0)
    temperature  = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    ph = models.FloatField(default=0)
    rainfall = models.FloatField(default=0)
    prediction = models.TextField(default='No Prediction')
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.prediction