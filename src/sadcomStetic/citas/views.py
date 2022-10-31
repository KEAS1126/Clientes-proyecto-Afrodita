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

def crearCita(request):
    if request.method=='POST':
        formulario_citas=FormularioCitas(request.POST)
        if formulario_citas.is_valid():
            formulario_citas.save()
            return redirect('/listarCitas/')
    else: 
        formulario_citas=FormularioCitas()
        contexto={'formulario_citas':formulario_citas}
        return render(request,'Citas/crearCitas.html',contexto)
    
    clienteDocumento= request.POST.get('documento')
    existe=Clientes.objects.filter(documento=clienteDocumento).exists()
    idCliente = Clientes.objects.filter(documento = clienteDocumento).values_list('idCliente', flat=True).first()
    if existe==False:
        error="El documento que ingreso no está registrado en el sistema"
        contexto={'formulario_citas':formulario_citas,"error":error}
        return render(request,'Citas/crearCitas.html',contexto)
    elif existe: 
        mensaje="el documento está registrado"
        contexto={'formulario_citas':formulario_citas,'idCliente':idCliente,'mensaje':mensaje}
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
    citas=AgendaCosto.objects.filter()
    contexto={"citas":citas,"cliente":cliente}
    return render(request,"Citas/verDetalleCita.html",contexto)


def formularioAgendaCosto(request,id):
    cliente=Clientes.objects.filter(idCliente=id)
    contexto={"cliente":cliente}
    return render(request,'Citas/crearCosto.html',contexto)
    
def crearAgendaCosto(request, id):

    clienteSesiones= request.POST['sesiones']
    clienteAbono= request.POST['abono']
    clienteCosto= request.POST['costo']

    if clienteAbono<clienteCosto:
        estado="Por pagar"
        costo=AgendaCosto(sesiones=clienteSesiones,abono=clienteAbono,costo=clienteCosto,estado=estado,idCliente=id)
        costo.save()
        return redirect('verDetalle-Cita', id)
    elif clienteAbono==clienteCosto:
        estado="Pagado"
        costo=AgendaCosto(sesiones=clienteSesiones,abono=clienteAbono,costo=clienteCosto,estado=estado,idCliente=id)
        costo.save()
        return redirect('verDetalle-Cita', id)
    elif clienteAbono>clienteCosto:
        mensaje="La cantidad que esta baonando es mayor alo que debe pagar"
        contexto={'mensaje':mensaje}
        return render(request,'Citas/crearCosto.html',contexto)





    # if request.method=='POST':
    #     formulario_agenda_costo=FormularioAgendaCosto(request.POST)
    #     if formulario_agenda_costo.is_valid():
    #         formulario_agenda_costo.save()
    #         return redirect('verDetalle-Cita', id)
    # else: 
    #     formulario_agenda_costo=FormularioAgendaCosto()
    
    # clienteAbono= formulario_agenda_costo.clean_abono('abono')
    # clienteCosto= formulario_agenda_costo.clean_costo('costo')
    # if clienteAbono<clienteCosto:
    #     estado="Por pagar"
    #     contexto={'estado':estado}
    #     return render(request,'Citas/crearCosto.html',contexto)
    # elif clienteAbono==clienteCosto:
    #     estado="Pagado"
    #     contexto={'estado':estado}
    #     return render(request,'Citas/crearCosto.html',contexto)
    # elif clienteAbono>clienteCosto:
    #     mensaje="La cantidad que esta baonando es mayor alo que debe pagar"
    #     contexto={'mensaje':mensaje}
    #     return render(request,'Citas/crearCosto.html',contexto)




    # contexto={'formulario_agenda_costo':formulario_agenda_costo,'idCliente':id}
    # return render(request,'Citas/crearCosto.html',contexto)
