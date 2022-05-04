from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Posteo(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150, default="-")
    texto = models.CharField(max_length=1000)
    autor = models.CharField(max_length=20, default="anonimo")
    imagenposteo = models.ImageField(upload_to="imagenesposteos",  null=True, blank=True)
   
    def __str__(self):
        return f"{self.titulo} | {self.subtitulo} | {self.texto} "

class Pais(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    capital = models.CharField(max_length=40) 

    def __str__(self):
        return f"{self.nombre} | {self.capital}"

class Foto(models.Model):
    id = models.IntegerField(primary_key=True)
    imagen = models.ImageField(upload_to="fotos",  null=True, blank=True)
    titulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.foto} | {self.titulo} | {self.descripcion}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

#class Message(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #asunto = models.CharField(max_length=100)
    #mensaje = models.CharField(max_length=1000)
    #receptor = models.ForeignKey(User, on_delete=models.CASCADE)