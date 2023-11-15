from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import sqlite3
from .forms import ClienteForm, LocalidadForm
from .models import Localidad, Persona


# Create your views here.
# def index(request):
#     return HttpResponse("Hola mundo desde Pycharm")

def index(request, template_name="entidad/index.html"):
    dato = {"nombre": "Emilia",
            "edad": 30,
            "direccion": {"calle": "Lavalle 1000", "localidad": "CABA"},
            "cant_hijos": 3,
            "hijos": ["Juan", "Ana", "Hector", "Sofía"]
            }
    return render(request, template_name, dato)


def acerca_de(request):
    return HttpResponse("Curso de Django - EducacionIT")


# def clientes(request):
#     conn = sqlite3.connect("contabilidad.sqlite")
#     cliente = conn.cursor()
#     cliente.execute("SELECT nombre, edad FROM personas")
#     html = """
#         <html>
#         <title> Lista de clientes </title>
#         <table style="border: 1px solid">
#         <thead>
#         <tr>
#         <th>Cliente</th>
#         <th>Edad</th>
#         </tr>
#         </thead>
#     """
#     for (nombre, edad) in cliente.fetchall():
#         html += "<tr><td>" + nombre + "</td><td>" + str(edad) + "</td></tr>"
#     html += "</table></html>"
#     conn.close()
#     return HttpResponse(html)

# def clientes(request, template_name="entidad/clientes.html"):
#     conn = sqlite3.connect("contabilidad.sqlite")
#     cliente = conn.cursor()
#     cliente.execute("SELECT nombre, edad FROM personas")
#     cliente_lista = cliente.fetchall()
#     conn.close()
#     dato = {"clientes": cliente_lista}
#     return render(request, template_name, dato)
#
#
# def cliente(request, nombre_cliente, template_name="entidad/cliente.html"):
#     conn = sqlite3.connect("contabilidad.sqlite")
#     cursor = conn.cursor()
#     cursor.execute("SELECT nombre, edad FROM personas WHERE nombre=?", [nombre_cliente])
#     cliente_s = cursor.fetchone()
#     if cliente_s is None:
#         raise Http404
#     conn.close()
#     dato = {"cliente": cliente_s}
#     return render(request, template_name, dato)
#
#
# def nuevo_cliente(request, template_name='entidad/nuevo_cliente.html'):
#     if request.method == 'POST':
#         form = ClienteForm(request.POST)
#         if form.is_valid():
#             conn = sqlite3.connect("contabilidad.sqlite")
#             cursor = conn.cursor()
#             cursor.execute("INSERT INTO personas VALUES (?, ?)",
#                            (form.cleaned_data["nombre"], form.cleaned_data["edad"]))
#             conn.commit()
#             conn.close()
#             return redirect('clientes')
#     else:
#         form = ClienteForm()
#     dato = {"form": form}
#     return render(request, template_name, dato)


# TRABAJO CON MODELS
# Listado
def localidades(request, template_name='entidad/localidades.html'):
    localidades_list = Localidad.objects.all()
    dato = {"localidades": localidades_list}
    return render(request, template_name, dato)


def clientes(request, template_name='entidad/clientes.html'):
    clientes_list = Persona.objects.all()
    dato = {"clientes": clientes_list}
    return render(request, template_name, dato)


# Alta de localidad (forma 1)
def nueva_localidad(request, template_name='entidad/localidad.html'):
    if request.method == 'POST':
        form = LocalidadForm(request.POST)
        if form.is_valid():
            Localidad.objects.create(nombre=form.cleaned_data["nombre"],
                                     cp=form.cleaned_data["cp"],
                                     provincia=form.cleaned_data["provincia"])
            return redirect("localidades")
    else:
        form = LocalidadForm()
    dato = {"form": form}
    return render(request, template_name, dato)


# Alta de cliente (forma 2 *** MAS UTILIZADA)
def nuevo_cliente(request, template_name='entidad/cliente.html'):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('clientes')
    else:
        form = ClienteForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def modificar_cliente(request, pk, template_name='entidad/cliente.html'):
    cliente = Persona.objects.get(id=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect("clientes")
    datos = {'form': form}
    return render(request, template_name, datos)


def eliminar_cliente(request, pk, template_name='entidad/cliente_confirmar_eliminacion.html'):
    cliente = Persona.objects.get(id=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
    dato = {'form': cliente}
    return render(request, template_name, dato)