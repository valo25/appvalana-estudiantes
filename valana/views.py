from datetime import datetime
from re import template
from django.http import HttpResponse
from django.shortcuts import render, redirect
from dataclasses import fields
from pyexpat import model

from valana.models import Posteo, Pais, Foto, Avatar
from valana.forms import  PosteoFormulario, UsuarioRegistroForm, UsuarioEditForm, AvatarFormulario, FotoFormulario


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def inicio(request):
 
    if request.user.is_authenticated:  
        avatar = Avatar.objects.filter(user=request.user)
        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
            dict_ctx = {"title": "Inicio", "page": "Inicio", "imagen_url": imagen}
        else:
            dict_ctx = {"title": "Inicio", "page": "Inicio"}
        return render(request, "valana/index.html", dict_ctx)
    else:
        return render(request, "valana/index.html")
    
def about(request):    
    if request.user.is_authenticated:  
        avatar = Avatar.objects.filter(user=request.user)
        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
            dict_ctx = {"title": "About", "page": "About", "imagen_url": imagen}
        else:
            dict_ctx = {"title": "About", "page": "About"}
        return render(request, "valana/about.html", dict_ctx)
    else:
        return render(request, "valana/about.html")
    

@login_required()
def paises(request):
    if request.user.is_authenticated:  
        avatar = Avatar.objects.filter(user=request.user)
        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
            dict_ctx = {"title": "Paises", "page": "Paises", "imagen_url": imagen}
            paises = Pais.objects.all()
            return render(request, "valana/paises.html", {"paises": paises, "title": "Paises", "page": "Paises", "imagen_url": imagen})
    
        else:
            dict_ctx = {"title": "Paises", "page": "Paises"}
        paises = Pais.objects.all()
        return render(request, "valana/paises.html", dict_ctx)
    else:
        paises = Pais.objects.all()
        return render(request, "valana/paises.html", {"paises": paises, "title": "Paises", "page": "Paises", "imagen_url": imagen})
  


@login_required()
def fotos(request):

    if request.user.is_authenticated:  
        avatar = Avatar.objects.filter(user=request.user)
        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
            dict_ctx = {"title": "Fotos", "page": "Fotos", "imagen_url": imagen}
        else:
            dict_ctx = {"title": "Fotos", "page": "Fotos"}
        fotos = Foto.objects.all()
        return render(request, "valana/fotos.html", dict_ctx)
    else:
        fotos = Foto.objects.all()
        return render(request, "valana/fotos.html", {"fotos": fotos, "title": "Fotos", "page": "Fotos", "imagen_url": imagen})
    

@login_required()
def posteos(request):
    
    avatar = Avatar.objects.filter(user=request.user)
    
    if len(avatar) > 0:
        imagen = avatar[0].imagen.url
    dict_ctx = {"title": "Inicio", "page": "Inicio", "imagen_url": imagen}
    posteos = Posteo.objects.all()
   # return render(request, "valana/posteos.html")

    if request.method == "POST":
        formulario = PosteoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            posteo = Posteo(data['titulo'], data['subtitulo'], data['texto'], data['imagenposteo'], data['autor'])
            posteo.save()

            return redirect("inicio")
    else:   
        
        formulario = PosteoFormulario()
        return render(request, "valana/posteo_list.html", {"posteos": posteos, "title": "Posteos", "page": "Posteos", "formulario": formulario, "imagen_url": imagen})

def buscar_posteo(request):
    avatar = Avatar.objects.filter(user=request.user)
    
    if len(avatar) > 0:
        imagen = avatar[0].imagen.url
    dict_ctx = {"title": "Inicio", "page": "Inicio", "imagen_url": imagen}
    data = request.GET.get('texto', "")
    error = ""

    if data:
        try:
            posteo = Posteo.objects.get(texto=data)
            return render(request, 'valana/busqueda_posteo.html', {"posteo": posteo, "id": data})

        except Exception as exc:
            print(exc)
            error = "No existe ese texto"
    return render(request, 'valana/busqueda_posteo.html', {"error": error})

def borrar_posteo(request, titulo_id):
    
    avatar = Avatar.objects.filter(user=request.user)
    
    if len(avatar) > 0:
        imagen = avatar[0].imagen.url
    
    dict_ctx = {"title": "Inicio", "page": "Inicio", "imagen_url": imagen}
    try:
        posteo = Posteo.objects.get(titulo = titulo_id)
        posteo.delete()

        return render(request, "valana/index.html")
    except Exception as exc:
        return render(request, "valana/index.html")

def actualizar_posteo(request, titulo_id):
    
    avatar = Avatar.objects.filter(user=request.user)
    
    if len(avatar) > 0:
        imagen = avatar[0].imagen.url
    
    dict_ctx = {"title": "Inicio", "page": "Inicio", "imagen_url": imagen}
    posteo = Posteo.objects.get(titulo=titulo_id)


    if request.method == "POST":
        formulario = PosteoFormulario(request.POST)
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            posteo.texto = informacion["texto"]
            posteo.save()
            return render(request, "valana/index.html", {"formulario": formulario})
 
    
    else:
        posteo = Posteo.objects.get(titulo=titulo_id)
        formulario = PosteoFormulario(initial={"titulo" : posteo.titulo, "texto" : posteo.texto})
        return render(request, "valana/update_posteo.html", {"formulario": formulario, "titulo_id":titulo_id})
 
class PosteoLista(LoginRequiredMixin, ListView):
    
    model = Posteo
    template_name = "valana/posteos_list.html"

class PosteoDetalle(DetailView):
    model = Posteo
    template_name = "valana/posteo_detalle.html"

class PosteoCrear(CreateView):
    model = Posteo
    success_url = "/pages/posteo/list"
    fields = ['titulo','subtitulo', 'texto', 'autor']

class PosteoActualizar(UpdateView):
    model = Posteo
    success_url = "/pages/posteo/list"
    fields = ['titulo', 'subtitulo', 'texto']

class PosteoBorrar(DeleteView):
    model = Posteo
    success_url = "/pages/posteo/list"

class PaisCrear(CreateView):
    model = Pais
    success_url = "/paises"
    fields = ['nombre', 'capital']

class PaisBorrar(DeleteView):
    model = Pais
    success_url = "/paises"

def login_request(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre_usuario = data.get("username")
            contrasenia = data.get("password")
            
            usuario = authenticate(username=nombre_usuario, password=contrasenia)

            if usuario is not None:
                login(request,usuario)
                dict_ctx = {"title": "Inicio", "page": usuario}
                return render(request, "valana/index.html", dict_ctx )
            else:
                dict_ctx = {"title": "Inicio", "page": usuario, "errors": ["El usuario no existe"]}

                return render(request, "valana/index.html", dict_ctx)

        else:
            dict_ctx= {"title": "Inicio", "page": "anonymous", "errors": ["Revise los datos ingresados"] }
            return render(request, "valana/index.html", dict_ctx)

    else:
        form = AuthenticationForm()
        return render(request, "valana/login.html", {"form": form})


def signup_request(request):
    
    if request.method == "POST":
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            form.save()

            return redirect("inicio")
        else:
            dict_ctx= {"title": "Inicio", "page": "anonymous", "errors": ["No pasó las validaciones"] }
            return render(request, "valana/index.html",dict_ctx)
    else:
        form = UsuarioRegistroForm()
        return render(request, "valana/signup.html", {"form": form})


@login_required()
def actualizar_usuario(request):
    
    avatar = Avatar.objects.filter(user=request.user)[0].imagen.url
    
    dict_ctx = {"title": "Inicio", "page": "Inicio", "imagen_url": "imagen"}
    usuario = request.user

    if request.method == "POST":
        formulario = UsuarioEditForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]

            usuario.save()
            return redirect("inicio")
        else:
            formulario = UsuarioEditForm(initial={"email": usuario.email})
            return render(request, "valana/editar_usuario.html", {"form": formulario, "errors": ["Datos invalidos"]})



    else: 
        formulario = UsuarioEditForm(initial={"email": usuario.email})
        return render(request, "valana/editar_usuario.html", {"form": formulario})

@login_required()
def cargar_avatar(request):

    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            usuario = request.user
            
            avatar = Avatar.objects.filter(user=usuario)

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()
            else:
                avatar = Avatar(user=usuario, imagen=formulario.cleaned_data["imagen"])
                avatar.save()
        return redirect("inicio")
    else:
        formulario = AvatarFormulario()
        return render(request, "valana/cargar_avatar.html", {"form": formulario})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def cargar_foto(request):
    if request.method == "POST":
        formulario = FotoFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            
            foto = Foto.objects.all()
           
            if len(foto) > 0:
                
                foto.imagen = formulario.cleaned_data["imagen"]
                foto.titulo = formulario.cleaned_data["titulo"]
                foto.descripcion = formulario.cleaned_data["descripcion"]
                foto.save()
            else:
                foto = Foto(foto, imagen=formulario.cleaned_data["imagen"])
                foto.save()
        return redirect("fotos")
    else:
        formulario = FotoFormulario()
        return render(request, "valana/cargar_foto.html", {"form": formulario} )

def profile(request):
    avatar = Avatar.objects.filter(user=request.user)
    
    if len(avatar) > 0:
        imagen = avatar[0].imagen.url

    dict_ctx = {"title": "Perfil", "page": "Perfil", "imagen_url": imagen}
    return render(request, "valana/profile.html", dict_ctx)

#def messages(request):
    #avatar = Avatar.objects.filter(user=request.user)
    
    #if len(avatar) > 0:
     #   imagen = avatar[0].imagen.url

    #dict_ctx = {"title": "Mensajes", "page": "Mensajes", "imagen_url": imagen}



    #if request.method == "POST":
        #formulario = MensajeFormulario(request.POST)

        #if formulario.is_valid():
        #    data = formulario.cleaned_data

       #     message = Message(data['asunto'], data['mensaje'], data['receptor'])
      #      message.save()

     #       return redirect("inicio")
    #else:   
        
        #formulario = MensajeFormulario()
        #return render(request, "valana/posteo_list.html", {"message": message, "title": "Mensajes", "page": "Mensajes", "formulario": formulario, "imagen_url": imagen})
