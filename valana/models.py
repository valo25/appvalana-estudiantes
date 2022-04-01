from django.db import models

# Create your models here.
class Posteo(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    texto = models.CharField(max_length=1000)

class Pais(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    capital = models.CharField(max_length=40)

class Imagen(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=500)
