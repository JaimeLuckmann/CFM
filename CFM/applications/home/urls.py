from django.urls import path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "home_app"

urlpatterns = [
    path('home',views.home,name="home"),
    # path('usuarios',views.usuario,name="usuarioshome"),
    path('usuarios',views.usuariosListView.as_view(),name="usuarios"),
    path('eliminar-usuario/<pk>',views.eliminarUsuarioDetailView.as_view(),name="eliminarUsuario"),
    path('editar-usuario/<pk>',views.usuarioUpdateView.as_view(),name="editarUsuario"),
]

urlpatterns += staticfiles_urlpatterns()