"""sadcomStetic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clientes.views import *
from citas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path(
        'listarCliente/',
        view=listarCliente, 
        name='listar-Cliente'
        ),

    path(
        'crearCliente/',
        view=crearCliente, 
        name='crear-Cliente'
        ),

    path(
        'editarCliente/<int:id>',
        view=editarCliente, 
        name='editar-Cliente'
        ),

    path(
        'eliminarCliente/<int:id>',
        view=eliminarCliente, 
        name='eliminar-Cliente'
        ),
    
    path(
        'verDetalleCliente/<int:id>',
        view=verDetalleCliente, 
        name='verDetalle-Cliente'
        ),

    path(
        'crearCorporal/<int:id>',
        view=crearCorporal, 
        name='crear-Corporal'
        ),

    path(
        'crearFacial/<int:id>',
        view=crearFacial, 
        name='crear-Facial'
        ),

    
    #Citas

     path(
        'listarCitas/',
        view=listarCita, 
        name='listar-Citas'
        ),

    path(
        'crearCitas/',
        view=crearCita, 
        name='crear-Citas'
        ),

    path(
        'editarCitas/<int:id>',
        view=editarCita, 
        name='editar-Citas'
        ),

    path(
        'eliminarCitas/<int:id>',
        view=eliminarCita, 
        name='eliminar-Citas'
        ),

    path(
        'verDetalleCita/<int:id>',
        view=verDetalleCita, 
        name='verDetalle-Cita'
        ),

    path(
        'formularioCosto/<int:id>',
        view=formularioAgendaCosto, 
        name='formulario-Agenda-Costo'
        ),

    path(
        'crearCosto/<int:id>',
        view=crearAgendaCosto, 
        name='Agenda-Costo'
        ),




]
