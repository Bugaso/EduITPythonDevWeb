from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("acerca-de", views.acerca_de, name='acerca_de'),
    # Localidad
    path("localidades", views.localidades, name='localidades'),
    path("nueva_localidad", views.nueva_localidad, name='nueva_localidad'),
    # Cliente
    path("clientes", views.clientes, name='clientes'),
    path("nuevo_cliente", views.nuevo_cliente, name='nuevo_cliente'),
    path("modificar_cliente/<int:pk>", views.modificar_cliente, name='modificar_cliente'),
    path("eliminar_cliente/<int:pk>", views.eliminar_cliente, name='eliminar_cliente')

]
