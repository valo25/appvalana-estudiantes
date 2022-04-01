from django.urls import path
from valana.views import *


urlpatterns = [
    path("", inicio, name = 'inicio'),
    path("paises/", paises, name = 'paises'),
    path("imagenes/", imagenes, name = 'imagenes'),
    path("posteos/", posteos, name = 'posteos'),
]