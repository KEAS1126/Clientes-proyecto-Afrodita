from django.shortcuts import render, redirect
from clientes.models import Clientes,EsteticoCorporal,ControlMedidas,EsteticoFacial
from django.views.generic import ListView
from clientes.forms import *

# Create your views here.

def listarCliente(request):
    clientes=Clientes.objects.filter()
    contexto={"clientes":clientes}
    return render(request,"Clientes/listarClientes.html",contexto)

def crearCliente(request):
    if request.method=='POST':
        formulario_cliente=FormularioCliente(request.POST)
        if formulario_cliente.is_valid():
            formulario_cliente.save()
            return redirect('/listarCliente/')
    else: 
        formulario_cliente=FormularioCliente()
    contexto={'formulario_cliente':formulario_cliente}
    return render(request,'Clientes/crearCliente.html',contexto)


def editarCliente(request,id):
    cliente=Clientes.objects.get(idCliente=id)
    if request.method=='GET':
        formulario_cliente=FormularioCliente(instance=cliente)
    else:
        formulario_cliente=FormularioCliente(request.POST,instance=cliente)
        if formulario_cliente.is_valid():
            formulario_cliente.save()
            return redirect('/listarCliente/')
    contexto={'formulario_cliente':formulario_cliente}
    return render(request,'Clientes/crearCliente.html',contexto)


def eliminarCliente(request,id):
    cliente=Clientes.objects.get(idCliente=id)
    cliente.delete()
    return redirect('/listarCliente/')

def verDetalleCliente(request, id):
    mostrar=Clientes.objects.filter(idCliente=id).first()
    corporal=EsteticoCorporal.objects.filter(idCliente=id) 
    facial=EsteticoFacial.objects.filter(idCliente=id) 
    contexto={"mostrar":mostrar,"corporal":corporal,"facial":facial}
    return render(request,"Clientes/VerDetalleCliente.html",contexto)

def crearCorporal(request, id):
    if request.method=='POST':
        formulario_corporal=FormularioCorporal(request.POST)
        if formulario_corporal.is_valid():
            formulario_corporal.save()
            return redirect("{% url 'verDetalle-Cliente' %}",id)
    else: 
        formulario_corporal=FormularioCorporal()
    contexto={'formulario_corporal':formulario_corporal,'idCliente':id}
    return render(request,'Clientes/crearCorporal.html',contexto)

def crearFacial(request, id):
    if request.method=='POST':
        formulario_facial=FormularioFacial(request.POST)
        if formulario_facial.is_valid():
            formulario_facial.save()
            return redirect("{% url 'verDetalle-Cliente' %}",id)
    else: 
        formulario_facial=FormularioFacial()
    contexto={'formulario_facial':formulario_facial,'idCliente':id}
    return render(request,'Clientes/crearFacial.html',contexto)
    
def verDetalleCorporal(request, id):
    mostrar=EsteticoCorporal.objects.filter(idCorporal=id).first()
    medidas=ControlMedidas.objects.filter(idCorporal=id)
    contexto={"mostrar":mostrar,"medidas":medidas}
    return render(request,"Clientes/VerDetalleCorporal.html",contexto)

def verDetalleFacial(request, id):
    mostrar=EsteticoFacial.objects.filter(idFacial=id).first()
    contexto={"mostrar":mostrar}
    return render(request,"Clientes/VerDetalleFacial.html",contexto)







class ListarClientes(ListView):
    model=Clientes
    template_name='clientes.html' 
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        clientes=Clientes.objects.filter()
        context['clientes']=clientes
        return context

    # def dispatch(self, request, *args, **kwargs):
    #     # if request.method=='GET':
    #     #     return redirect()
    #     return super().dispatch(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return redirect()

class CrearCliente(ListView):
    model=Clientes
    template_name:'crearCliente.html'

    def post(self, request, *args, **kwargs):
        nombreCliente=request.POST['nombre']
        documentoCliente=request.POST['documento']
        sexoCliente=request.POST['sexo']
        telefonoCliente=request.POST['telefono']
        direccionCliente=request.POST['direccion']
        correoCliente=request.POST['correo']
        fechaNacimientoCliente=request.POST['fechaNacimiento']
        estadoCivilCliente=request.POST['estadoCivil']
        numeroHijosCliente=request.POST['numeroHijos']
        clientes=Clientes(nombre=nombreCliente,documento=documentoCliente,sexo=sexoCliente,telefono=telefonoCliente,direccion=direccionCliente,correo=correoCliente,fechaNacimiento=fechaNacimientoCliente,estadoCivil=estadoCivilCliente,numeroHijos=numeroHijosCliente)
        clientes.save()
        return redirect("/listarclientes/")
        
class EditarCliente(ListView):
    model=Clientes
    template_name='editarCliente.html' 
    id=id
    
    def dispatch(self, request, *args, **kwargs):
        self.id=self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        self.id=self.get_object()
        clientes=Clientes.objects.filter(idCliente=id).first()
        context['clientes']=clientes
        return context

    def post(self, request, *args, **kwargs):
        nombreCliente=request.GET['nombre']
        documentoCliente=request.GET['documento']
        sexoCliente=request.GET['sexo']
        telefonoCliente=request.GET['telefono']
        direccionCliente=request.GET['direccion']
        correoCliente=request.GET['correo']
        fechaNacimientoCliente=request.GET['fechaNacimiento']
        estadoCivilCliente=request.GET['estadoCivil']
        numeroHijosCliente=request.GET['numeroHijos']
        actualizar=Clientes.objects.get(idCliente=id)
        actualizar.nombre=nombreCliente
        actualizar.documento=documentoCliente
        actualizar.sexo=sexoCliente
        actualizar.telefono=telefonoCliente
        actualizar.direccion=direccionCliente
        actualizar.correo=correoCliente
        actualizar.fechaNacimiento=fechaNacimientoCliente
        actualizar.estadoCivil=estadoCivilCliente
        actualizar.numeroHijos=numeroHijosCliente
        actualizar.save()
        return redirect("/listarclientes/")

def formularioControlMedidas(request,id):
    corporal=EsteticoCorporal.objects.filter(idCorporal=id).first()
    contexto={"corporal":corporal}
    return render(request,"crearControlMedidas.html",contexto)


def crearControMedidas(request,id):
    crearIdC=EsteticoCorporal.objects.get(idCorporal=id)
    #Control medidas
    fechaMedida=request.GET['fecha']
    brazoDMedida=request.GET['brazoD']
    brazoIMedida=request.GET['brazoI']
    abdomenAMedida=request.GET['abdomenA']
    cinturaMedida=request.GET['cintura']
    abdomenBMedida=request.GET['abdomenB']
    piernaDMedida=request.GET['piernaD']
    piernaIMedida=request.GET['piernaI']
    medidas=ControlMedidas(fecha=fechaMedida,brazoD=brazoDMedida,brazoI=brazoIMedida,abdomenA=abdomenAMedida,cintura=cinturaMedida,abdomenB=abdomenBMedida,piernaD=piernaDMedida,piernaI=piernaIMedida,idCorporal=crearIdC)
    medidas.save()
    return redirect("verDetalleCorporal",id)

def buscar(request):
    buscarCliente=request.POST['buscar']
    cliente=Clientes.objects.filter(nombre=buscarCliente)
    contexto={"buscar":buscarCliente,"cliente":cliente}
    return(request,"clientes.html",contexto)








