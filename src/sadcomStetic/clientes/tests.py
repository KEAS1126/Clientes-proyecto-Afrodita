from django.test import TestCase
from sadcomStetic.sadcomStetic import wsgi
from models import Clientes

# Create your tests here.

#listar
query=Clientes.objects.all()
print(query)

#crear
crear=Clientes(nombre="Kevin Estiven",sexo="m")
crear.save()

#editar
editar=Clientes.objects.get(pk=1)
editar.nombre="Sandra Viviana"
editar.sexo="f"
editar.save()

#eliminar

eliminar=Clientes.objects.get(pk=1)
eliminar.delete()

#filtros

filtros=Clientes.objects.filter(pk=1)

for i in filtros:
    print(i.name)