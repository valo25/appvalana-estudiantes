from collections import UserList
from dataclasses import fields
import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PosteoFormulario(forms.Form):
    titulo = forms.CharField(max_length=100)
    texto = forms.CharField(max_length=1000)

class PaisFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    capital = forms.CharField(max_length=40)


class UsuarioRegistroForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Constrasenia 1", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Constrasenia 2", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = { k: "" for k in fields}



class UsuarioEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Constrasenia 1", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Constrasenia 2", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
        help_text = { k: "" for k in fields}

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField()

class FotoFormulario(forms.Form):
    imagen = forms.ImageField()
    titulo = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=200)

#class MensajeFormulario(forms.Form):
 #   asunto = forms.CharField(max_length=100)
  #  mensaje = forms.CharField(max_length=1000)
   # receptor = forms.SelectMultiple(UserList)