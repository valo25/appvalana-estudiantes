
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class PosteoFormulario(forms.Form):

    titulo = forms.CharField(max_length=100)
    texto = forms.CharField(max_length=1000)

class PaisFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    capital = forms.CharField(max_length=40)

class ImagenFormulario(forms.Form):
    titulo = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=500)



class UsuarioRegistroForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia 1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Contrasenia 2', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = { k: "" for k in fields}


class UsuarioEditForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia 1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Contrasenia 2', widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'password1', 'password2']
        help_text = { k: "" for k in fields}


class AvatarFormulario(forms.Form):

    imagen = forms.ImageField()