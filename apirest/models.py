
from django.db import models
from django.contrib.postgres.fields import FloatRangeField

# Create your models here.
class Sensores(models.Model):
    temperatura = models.FloatField()
    peso =  models.FloatField()
    humedad = models.IntegerField()

