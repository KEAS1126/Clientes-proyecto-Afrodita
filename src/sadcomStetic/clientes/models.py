from django.db import models

# Create your models here.

# class SexoOpciones(models.Model):
#     hombre=models.CharField(max_length=100)
#     mujer=models.CharField(max_length=100)

#     def __str__(self):
#         return '{} {}'.format(self.hombre,self.mujer)
    

class Clientes(models.Model):
    idCliente=models.AutoField(primary_key=True)
    fechaCreacion=models.DateTimeField(auto_now_add=True)
    nombre=models.CharField(max_length=60)
    sexo=models.CharField(max_length=10)
    documento=models.CharField(max_length=10)
    fechaNacimiento=models.CharField(max_length=10)
    telefono=models.CharField(max_length=10,blank=True,null=True )
    direccion=models.CharField(max_length=100,blank=True,null=True)
    correo=models.EmailField(blank=True,null=True)
    estadoCivil=models.CharField(max_length=11)
    numeroHijos=models.CharField(max_length=2)
    fechaActualizacion=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return '{}'.format(self.documento)

class EsteticoCorporal(models.Model):
    
    idCorporal=models.AutoField(primary_key=True)
    idCliente=models.ForeignKey(Clientes,on_delete=models.PROTECT)
    fechaCreacion=models.DateTimeField(auto_now_add=True)
    nombreE=models.CharField(max_length=60)

class ControlMedidas(models.Model):
    idMedidas=models.AutoField(primary_key=True)
    idCorporal=models.ForeignKey(EsteticoCorporal, null=True, on_delete=models.PROTECT)
    fecha=models.CharField(max_length=10)
    brazoD=models.CharField(max_length=7)
    brazoI=models.CharField(max_length=7)
    abdomenA=models.CharField(max_length=7)
    cintura=models.CharField(max_length=7)
    abdomenB=models.CharField(max_length=7)
    piernaD=models.CharField(max_length=7)
    piernaI=models.CharField(max_length=7)

class EsteticoFacial(models.Model):
    idFacial=models.AutoField(primary_key=True)
    idCliente=models.ForeignKey(Clientes, null=True, on_delete=models.PROTECT)
    fechaCreacion=models.DateTimeField(auto_now_add=True)
    nombreE=models.CharField(max_length=60)
    #Factores agravantes
    tratamientoM=models.CharField(max_length=2)
    cualTM=models.TextField()
    sustitucionH=models.CharField(max_length=2)
    tomaA=models.CharField(max_length=2)
    drogas=models.CharField(max_length=2)
    alimentosP=models.TextField()
    alimentosR=models.TextField()
    fuma=models.CharField(max_length=2)
    tomaL=models.CharField(max_length=2)
    protegeS=models.CharField(max_length=2)
    duermeB=models.CharField(max_length=2)
    menopausia=models.CharField(max_length=2)
    medicamentosOT=models.CharField(max_length=2)
    cualesOT=models.TextField()
    padeceE=models.CharField(max_length=2)
    cancerP=models.CharField(max_length=2)
    asma=models.CharField(max_length=2)
    lupus=models.CharField(max_length=2)
    herpes=models.CharField(max_length=2)
    hepatitis=models.CharField(max_length=2)
    epilepsias=models.CharField(max_length=2)
    dolorC=models.CharField(max_length=2)
    ampollasF=models.CharField(max_length=2)
    tiroides=models.CharField(max_length=2)
    problemasC=models.CharField(max_length=2)
    psicologicos=models.CharField(max_length=2)
    urinarios=models.CharField(max_length=2)
    nasales=models.CharField(max_length=2)
    digestivos=models.CharField(max_length=2)
    #Está utilizando o uso
    alfahidroxiacidos=models.CharField(max_length=2)
    retinA=models.CharField(max_length=2)
    differin=models.CharField(max_length=2)
    accutane=models.CharField(max_length=2)
    motivoC=models.TextField()
    productoCM=models.TextField()
    #Analisis de piel
    normal=models.CharField(max_length=2)
    gruesa=models.CharField(max_length=2)
    aspera=models.CharField(max_length=2)
    suave=models.CharField(max_length=2)
    normal1=models.CharField(max_length=2)
    cerrado=models.CharField(max_length=2)
    dilatado=models.CharField(max_length=2)
    #Brillo
    zonasM=models.CharField(max_length=2)
    zonasB=models.CharField(max_length=2)
    #Grado de hidratación
    normal2=models.CharField(max_length=2)
    deshidratada=models.CharField(max_length=2)
    hiperdeshidratada=models.CharField(max_length=2)
    #Fototipo de piel
    fototipoP=models.CharField(max_length=10)
    #Alteraciones del envejecimiento
    lineasF=models.CharField(max_length=2)
    profundas=models.CharField(max_length=2)
    flacidez=models.CharField(max_length=2)
    parpados=models.CharField(max_length=2)
    cuello=models.CharField(max_length=2)
    nasogenianos=models.CharField(max_length=2)
    labios=models.CharField(max_length=2)
    #Acné(desde cuándo)
    comedones=models.CharField(max_length=2)
    milias=models.CharField(max_length=2)
    quistes=models.CharField(max_length=2)
    #Pigmentación
    melasma=models.CharField(max_length=2)
    hipercromia=models.CharField(max_length=2)
    edema=models.CharField(max_length=2)
    grasa=models.CharField(max_length=2)
    #Cuidados que realiza diariamente
    rutinasH=models.TextField()
    cuidadosH=models.TextField()
    mensuales=models.CharField(max_length=2)
    productoH=models.TextField()

    

    
    

    

    
    
    
    
    
    
    
    
    

    
    # fecha=models.DateField()
    # brazoIzquierdo=models.CharField(max_length=10)
    # brazoDerecho=models.CharField(max_length=10)
    # abdomenAlto=models.CharField(max_length=10)
    # cintura=models.CharField(max_length=10)
    # abdomenBajo=models.CharField(max_length=10)
    # piernaIzquierda=models.CharField(max_length=10)
    # piernaDerecha=models.CharField(max_length=10)
    

