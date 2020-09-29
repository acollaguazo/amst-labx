
from django.db import models

class Sensores(models.Model):
    temperatura = models.FloatField()
    peso =  models.FloatField()
    humedad = models.IntegerField()

