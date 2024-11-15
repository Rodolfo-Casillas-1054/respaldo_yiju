from django.urls import path
from enmarcados_app import views

urlpatterns = [
    path('', views.Inicio_vista, name='Inicio_vista'),
    path('RegistrarCliente/' ,views.RegistrarCliente, name='RegistrarCliente' ),
    path("SeleccionarCliente/<id>",views.SeleccionarCliente,name="SeleccionarCliente"),
    path("EditarCliente/",views.EditarCliente,name="EditarCliente"),
    path("BorrarCliente/<id>",views.BorrarCliente,name="BorrarCliente")
]