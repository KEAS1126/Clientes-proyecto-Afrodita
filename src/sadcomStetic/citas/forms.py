from datetime import datetime
from django import forms
from citas.models import *
from django.forms import ValidationError

class FormularioCitas(forms.ModelForm):
    # def clean_fechaCita(self):
    #     fechaCita=self.cleaned_data['fechaCita']
    #     actual=datetime.now()
    #     actualStr=actual.strftime('%Y-%m-%d')
    #     if fechaCita<actualStr:
    #         raise  ValidationError("Error. se esta eligiendo una fecha de dias anteriores")
    #     return fechaCita

    class Meta:
        model=Citas
        fields='__all__'
        estadoCita=(
            ('Espera','Espera'),
            ('Proceso','Proceso'),
            ('Cancelado','Cancelado'),
            ('Finalizado','Finalizado'),
            )
        widgets={   
            'fechaCita':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre completo','type':'date'}),
            'estado':forms.Select(choices=estadoCita,attrs={'class':'form-select'}),
            'idCliente':forms.TextInput(attrs={'hidden':''}),
        }

# class FormularioAgendaCosto(forms.ModelForm):
#     def clean_costo(self,costo):
#         costo=self.cleaned_data['costo']
#         return costo
#     def clean_abono(self,abono):
#         abono=self.cleaned_data['abono']

#         return abono
#     class Meta:
#         model=AgendaCosto
#         fields='__all__'
#         widgets={   
#             'sesiones':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el Número de sesiones'}),
#             'costo':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el costo del servicio'}),
#             'abono':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el abono del servicio'}),
#         }

class FormularioAgendaFecha(forms.ModelForm):
    class Meta:
        model=AgendaFecha
        fields='__all__'
        widgets={   
            'FechaAgenda':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la fecha de las sesión'}),
        }
        
        
