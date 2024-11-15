from django.shortcuts import render, redirect
from .models import Materia

# Create your views here.

def Inicio_vista(request):
    lasmaterias=Materia.objects.all()
    return render(request, 'gestionarmateria.html', {'mismaterias' : lasmaterias})

def RegistrarCliente(request):
    id=request.POST['txtid']
    nombre=request.POST['txtnombre']
    apellido=request.POST['txtapellido']
    edad=request.POST['numedad']
    telefono=request.POST['numtelefono']

    guardarmaterias=Materia.objects.create(id=id, nombre=nombre, apellido=apellido, edad=edad, telefono=telefono)
    return redirect ("/")



def EditarCliente(request):
    id=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    apellido=request.POST['txtapellido']
    edad=request.POST['numedad']
    telefono=request.POST['numtelefono']

    cliente=Materia.objects.get(id=id)
    cliente.nombre=nombre
    cliente.apellido=apellido
    cliente.edad=edad
    cliente.telefono=telefono
    cliente.save()
    return redirect ("/")

def SeleccionarCliente(request,id):
    cliente=Materia.objects.get(id=id)
    return render(request,"EditarMateria.html",{"mismaterias":cliente})

def BorrarCliente(request,id):
    cliente=Materia.objects.get(id=id)
    cliente.delete()
    return redirect("/")