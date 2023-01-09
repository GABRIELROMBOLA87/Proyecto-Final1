from django.db import models

# Create your models here.

class Post(models.Model):
    Repuesto = models.CharField(max_length=100)
    Vehiculo = models.CharField(max_length=100)
    Detalle = models.TextField(max_length=3000)
    #Precio = models.CharField(max_length=10)


