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
from clientes.views import saludo, cliente, editar, actualizar, verDetalleCliente,verDetalleCorporal,verDetalleFacial, crearCliente, crearCorporal,crearControMedidas, formularioCliente, formularioCorporal,formularioControlMedidas,crearFacial,formularioFacial , formularioClientes,saludo1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',saludo),
    path('cliente/',cliente),
    path('editar/<int:id>',editar, name='editarCliente'),
    path('actualizar/<int:id>',actualizar, name='actualizarCliente'),
    path('verDetalleCliente/<int:id>',verDetalleCliente, name='verDetalleCliente'),
    path('verDetalleCorporal/<int:id>',verDetalleCorporal, name='verDetalleCorporal'),
    path('verDetalleFacial/<int:id>',verDetalleFacial, name='verDetalleFacial'),
    path('crearCliente/',crearCliente),
    path('formularioCliente/',formularioCliente),
    path('crearCorporal/<int:id>',crearCorporal, name='crearCorporal'),
    path('crearControMedidas/<int:id>',crearControMedidas, name='crearControMedidas'),
    path('formularioCorporal/<int:id>',formularioCorporal, name='formularioCorporal'),
    path('formularioControlMedidas/<int:id>',formularioControlMedidas, name='formularioControlMedidas'),
    path('crearFacial/<int:id>',crearFacial,name='crearFacial'),
    path('formularioFacial/<int:id>',formularioFacial,name='formularioFacial'),
    path('listaClientes/',formularioClientes.as_view(),name='formularioFacial'),
    path('saludo1/',view=saludo1,name='saludo'),
    
]
