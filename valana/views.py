from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from dataclasses import fields
from pyexpat import model

from valana.models import Posteo
from valana.forms import PosteoFormulario

def intentobusqueda(request):
    return render(request, "valana/intentobusqueda.html")

# Create your views here.
def inicio(request):
    date_init = datetime.now()
    dict_user = {"user": "anamornig", "date_init":date_init}
    return render(request, "valana/index.html", dict_user)

def paises(request):
    return render(request, "valana/paises.html")

def imagenes(request):
    return render(request,"valana/imagenes.html")

def posteos(request):
    return render(request, "valana/posteos.html")

    posteos = Posteo.objects.all()

    if request.method == "POST":
        formulario = PosteoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            posteo = Posteo(data['titulo'], data['texto'])
            posteo.save()

            return redirect('Inicio')
    else:   
        
        formulario = PosteoFormulario()
        return render(request, "valana/posteos.html", {"posteos": posteos, "title": "Posteos", "page": "Posteos", "formulario": formulario})

def buscar_posteo(request):

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

def borrar_posteo(request, id):
    try:
        posteo = Posteo.objects.get(texto=id)
        posteo.delete()

        return render(request, "valana/index.html")
    except Exception as exc:
        return render(request, "valana/index.html")

def actualizar_posteo(request, id):

    posteo = Posteo.objects.get(texto=id)


    if request.method == "POST":
        formulario = PosteoFormulario(request.POST)
        
        if formulario.is_valid():

            informacion = formulario.cleaned_data


            posteo.titulo = informacion["titulo"]
            
            posteo.save()

            return render(request, "valana/index.html")

    else:

        formulario = PosteoFormulario(initial={"titulo": posteo.titulo, "texto": posteo.texto})

        return render(request, "valana/update_posteo.html", {"formulario": formulario, "id": id})


#class PosteoLista(LoginRequiredMixin, ListView):

 #   model = Posteo
  #  template_name = "valana/posteos_list.html"

#class PosteoDetalle(DetailView):

 #   model = Posteo
  #  template_name = "valana/posteo_detalle.html"

#class PosteoCrear(CreateView):

 #   model = Posteo
  #  success_url = "/valana/posteo/list"
   # fields = ['titulo', 'texto']

#class PosteoActualizar(UpdateView):

 #   model = Posteo
  #  success_url = "/valana/posteo/list"
   # fields = ['titulo']


#class PosteoBorrar(DeleteView):

 #   model = Posteo
  #  success_url = "/valana/posteo/list"

