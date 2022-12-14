from django.shortcuts import render, redirect
from citas.models import *
from citas.forms import *
from clientes.models import Clientes
from django import forms

# Create your views here.

def listarCita(request):
    citas=Citas.objects.filter()
    contexto={"citas":citas}
    return render(request,"Citas/listarCitas.html",contexto)

def verificarDocumento(request):
    clienteDocumento= request.POST.get('documento')
    existe=Clientes.objects.filter(documento=clienteDocumento).exists()
    idCliente = Clientes.objects.filter(documento = clienteDocumento).values_list('idCliente', flat=True).first()
    
    if existe: 
        return redirect('crear-Citas',idCliente)

    else:
        error="El documento que ingreso no está registrado en el sistema"
        contexto={"error":error}
        return render(request,'Citas/verificarDocumento.html',contexto)
    
    

def crearCita(request,id):
    if request.method=='POST':
        formulario_citas=FormularioCitas(request.POST)
        if formulario_citas.is_valid():
            formulario_citas.save()
            return redirect('/listarCitas/')
    else: 
        formulario_citas=FormularioCitas()
        
    contexto={'formulario_citas':formulario_citas,'idCliente':id}
    return render(request,'Citas/crearCitas.html',contexto)
    
    
    
def editarCita(request,id):
    citas=Citas.objects.get(idCita=id)
    if request.method=='GET':
        formulario_citas=FormularioCitas(instance=citas)
    else:
        formulario_citas=FormularioCitas(request.POST,instance=citas)
        if formulario_citas.is_valid():
            formulario_citas.save()
            return redirect('/listarCitas/')
    contexto={'formulario_citas':formulario_citas}
    return render(request,'Citas/editarCitas.html',contexto)

def eliminarCita(request,id):
    cita=Citas.objects.get(idCita=id)
    cita.delete()
    return redirect('/listarCitas/')

def verDetalleCita(request, id):
    cliente=Clientes.objects.filter(idCliente=id).first()
    agendaCosto=AgendaCosto.objects.filter(idCliente=id)
    contexto={"agendaCosto":agendaCosto,"cliente":cliente}
    return render(request,"Citas/verDetalleCita.html",contexto)

def crearAgendaCosto(request, id):

    if request.method=='POST':
        formulario_agenda_costo=FormularioAgendaCosto(request.POST)
        if formulario_agenda_costo.is_valid():
            formulario_agenda_costo.save()
            return redirect('verDetalle-Cita', id)
    else: 
        formulario_agenda_costo=FormularioAgendaCosto()
    
    contexto={'formulario_agenda_costo':formulario_agenda_costo,'idCliente':id}
    return render(request,'Citas/crearCosto.html',contexto)

def editarAgendaCosto(request,id):
    agendaCosto=AgendaCosto.objects.get(idAgendaCosto=id)
    if request.method=='GET':
        formulario_agenda_costo=FormularioAgendaCosto(instance=agendaCosto)
    else:
        formulario_agenda_costo=FormularioAgendaCosto(request.POST,instance=agendaCosto)
        if formulario_agenda_costo.is_valid():
            formulario_agenda_costo.save()
            return redirect('verDetalle-Cita', id)
    contexto={'formulario_agenda_costo':formulario_agenda_costo}
    return render(request,'Citas/editarCosto.html',contexto)

def verDetalleCosto(request, id):
    agendaCosto=AgendaCosto.objects.filter(idAgendaCosto=id).first()
    agendaFecha=AgendaFecha.objects.filter(idAgendaCosto=id)
    contexto={"agendaFecha":agendaFecha,"agendaCosto":agendaCosto}
    return render(request,"Citas/verDetalleCosto.html",contexto)

def crearAgendaFecha(request, id):
    if request.method=='POST':
        formulario_agenda_fecha=FormularioAgendaFecha(request.POST)
        if formulario_agenda_fecha.is_valid():
            formulario_agenda_fecha.save()
            return redirect('verDetalle-Costo', id)
    else: 
        formulario_agenda_fecha=FormularioAgendaFecha()

    agendacosto=AgendaCosto.objects.filter(idAgendaCosto=id)
    for listar in agendacosto:

        clienteCosto=listar.costo
        clienteAbono=listar.abono


        if clienteAbono<clienteCosto:
            estado="Por pagar"
            contexto={'estado':estado,'formulario_agenda_fecha':formulario_agenda_fecha,'idAgendaCosto':id}
            return render(request,'Citas/crearFecha.html',contexto)
        elif clienteAbono==clienteCosto:
            estado="Pagado"
            contexto={'estado':estado,'formulario_agenda_fecha':formulario_agenda_fecha,'idAgendaCosto':id}
            return render(request,'Citas/crearFecha.html',contexto)
        else :
            estado="Debe"
            contexto={'estado':estado,'formulario_agenda_fecha':formulario_agenda_fecha,'idAgendaCosto':id}
            return render(request,'Citas/crearFecha.html',contexto)

        
    contexto={'formulario_agenda_fecha':formulario_agenda_fecha}
    return render(request,'Citas/crearFecha.html',contexto)
        # agendafecha=AgendaFecha.objects.filter(idAgendaCosto=id)

        # contador=0
        # while contador<agendafecha:
        #     contador+=1

        
        # if contador==clienteSesiones:
        #     error='El número de sesiones es superior'
        #     contexto={'error':error}
        #     render(request,'Citas/crearFecha.html',contexto)


            


    

        
        
    
    
    