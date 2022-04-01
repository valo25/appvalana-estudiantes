from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render


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
    return render(request, 'valana/posteos.html')

#def formulario_curso(request):
 #   if request.method == "POST":
  #      curso = Curso(request.POST['nombre'], request.POST['camada'])
   #     curso.save()
    
   # return render(request, 'valana/cursosFormulario.html')