from django.urls import path
from .views import Inicio, EditarNota, EliminarNota, VerNota, CrearNota

urlpatterns = [
    path("", Inicio.as_view(), name="home"),
    path("editar_nota/<int:pk>", EditarNota.as_view(), name="editar_nota"),
    path("nota_eliminar/<int:pk>", EliminarNota.as_view(), name="eliminar_nota"),
    path("ver_nota/<int:pk>", VerNota.as_view(), name="ver_nota"),
    path("crear_nota", CrearNota.as_view(), name="crear_nota"),
]
