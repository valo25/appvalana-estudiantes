from django.urls import path
from valana.views import *
from unicodedata import name
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", inicio, name = 'inicio'),

    path("accounts/login/", login_request, name="login"),
    path("accounts/signup/", signup_request, name="signup"),
    path("accounts/logout/", LogoutView.as_view(template_name="valana/accounts/logout.html"), name="logout"),


    path("paises/", paises, name = 'paises'),
    path("paises/crearpais", PaisCrear.as_view(), name ='crear_pais'),
    path("paises/borrarpais/<pk>/", PaisBorrar.as_view(), name = 'pais_borrar'),

    path("fotos/", fotos, name = 'fotos'),
    path("cargar_foto/", cargar_foto, name="CargarFoto"),

    path("pages/posteos/", posteos, name = 'posteos'),
    path("pages/buscarposteo/", buscar_posteo, name = "BuscarPosteo"),
    path("pages/borrarposteo/<titulo_id>/", borrar_posteo, name= "eliminarPosteo"),
    path("pages/update_posteo/<titulo_id>/", actualizar_posteo),


    path("pages/posteo/list/", PosteoLista.as_view(), name="posteo_list"),
    path("pages/posteo/nuevo/", PosteoCrear.as_view(), name="posteo_create"),
    path("pages/posteo/detalle/<pk>/", PosteoDetalle.as_view(), name="posteo_detail"),
    path("pages/posteo/editar/<pk>/", PosteoActualizar.as_view(), name="posteo_update"),
    path("pages/posteo/borrar/<pk>/", PosteoBorrar.as_view(), name="posteo_delete"),

    path("accounts/actualizar_usuario/", actualizar_usuario, name="EditarUsuario"),
    path("accounts/cargar_avatar/", cargar_avatar, name="CargarAvatar"),
    path("accounts/profile/", profile, name="profile" ),

    path("about/", about, name="about" )
    


] 