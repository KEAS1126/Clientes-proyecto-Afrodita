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
from clientes.views import saludo, cliente, editar, actualizar, verDetalleCliente,verDetalleCorporal,verDetalleFacial, crearCliente, crearCorporal,crearControMedidas, formularioCliente, formularioCorporal,formularioControlMedidas,crearFacial,formularioFacial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',saludo),
    path('cliente/',cliente),
    path('editar/<int:idCliente>',editar, name='editarCliente'),
    path('actualizar/<int:idCliente>',actualizar, name='actualizarCliente'),
    path('verDetalleCliente/<int:idCliente>',verDetalleCliente, name='verDetalleCliente'),
    path('verDetalleCorporal/<int:idCorporal>',verDetalleCorporal, name='verDetalleCorporal'),
    path('verDetalleFacial/<int:idFacial>',verDetalleFacial, name='verDetalleFacial'),
    path('crearCliente/',crearCliente),
    path('formularioCliente/',formularioCliente),
    path('crearCorporal/<int:idCliente>',crearCorporal, name='crearCorporal'),
    path('crearControMedidas/<int:idCorporal>',crearControMedidas, name='crearControMedidas'),
    path('formularioCorporal/<int:idCliente>',formularioCorporal, name='formularioCorporal'),
    path('formularioControlMedidas/<int:idCorporal>',formularioControlMedidas, name='formularioControlMedidas'),
    path('crearFacial/<int:idCliente>',crearFacial,name='crearFacial'),
    path('formularioFacial/<int:idCliente>',formularioFacial,name='formularioFacial'),
    
]
