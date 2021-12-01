from django.db import models
from django.utils import timezone


class compus(models.Model):
    marca  =   models.CharField(max_length=150)
    detalle  =   models.CharField(max_length=150)
    precio  =   models.CharField(max_length=150)
    def __str__(self):
        return self.marca
