from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posteo(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=100)
    texto = models.CharField(max_length=1000)
    
    def __str__(self):
        return f"{self.titulo}"

class Pais(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    capital = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} | {self.capital}"

class Foto(models.Model):
    id = models.IntegerField(primary_key=True)
    foto = models.ImageField(upload_to="fotos",  null=True, blank=True)
    titulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=500)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
