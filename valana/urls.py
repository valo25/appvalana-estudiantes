from django.urls import path
from valana.views import *
from unicodedata import name
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", inicio, name = 'inicio'),

    path("login/", login_request, name="login"),
    path("register/", register_request, name="register"),
    path("logout/", LogoutView.as_view(template_name="valana/logout.html"), name="logout"),


    path("paises/", paises, name = 'paises'),

    path("fotos/", fotos, name = 'fotos'),
    path("cargar_foto/", cargar_foto, name="CargarFoto"),

    path("posteos/", posteos, name = 'posteos'),
    path("buscarposteo/", buscar_posteo, name = "BuscarPosteo"),
    path("borrarposteo/<titulo_id>/", borrar_posteo, name= "eliminarPosteo"),
    path("update_posteo/<titulo_id>/", actualizar_posteo),


    path("posteo/list/", PosteoLista.as_view(), name="posteo_list"),
    path("posteo/nuevo/", PosteoCrear.as_view(), name="posteo_create"),
    path("posteo/detalle/<pk>/", PosteoDetalle.as_view(), name="posteo_detail"),
    path("posteo/editar/<pk>/", PosteoActualizar.as_view(), name="posteo_update"),
    path("posteo/borrar/<pk>/", PosteoBorrar.as_view(), name="posteo_delete"),

    path("actualizar_usuario/", actualizar_usuario, name="EditarUsuario"),
    path("cargar_avatar/", cargar_avatar, name="CargarAvatar"),
    path("profile/", profile, name="profile" ),

    path("about/", about, name="about" )
    


] 