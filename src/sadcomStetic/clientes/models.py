from django.db import models

# Create your models here.

class Clientes(models.Model):
    idCliente=models.AutoField(primary_key=True)
    fechaCreacion=models.DateTimeField(auto_now_add=True)
    nombre=models.CharField(max_length=60)
    sexo=models.CharField(max_length=9, blank=True,null=True)
    documento=models.CharField(max_length=10)
    fechaNacimiento=models.CharField(max_length=10)
    telefono=models.CharField(max_length=10,blank=True,null=True )
    direccion=models.CharField(max_length=100,blank=True,null=True)
    correo=models.EmailField(blank=True,null=True)
    estadoCivil=models.CharField(max_length=11)
    numeroHijos=models.CharField(max_length=2)
    fechaActualizacion=models.DateTimeField(auto_now=True)
    
class EsteticoCorporal(models.Model):
    
    idCorporal=models.AutoField(primary_key=True)
    idCliente=models.ForeignKey(Clientes,on_delete=models.PROTECT)
    fechaCreacion=models.DateTimeField(auto_now_add=True)
    nombreE=models.CharField(max_length=60)
    #Sufre problemas
    tensionA=models.CharField(max_length=2)
    digestivo=models.CharField(max_length=2)
    circulacion=models.CharField(max_length=2)
    endrocrino=models.CharField(max_length=2)
    cardiacos=models.CharField(max_length=2)
    otrosP=models.TextField()
    #Peso actual
    kilos=models.CharField(max_length=7)
    talla=models.CharField(max_length=7)
    altura=models.CharField(max_length=7)
    masaC=models.CharField(max_length=7)
    siluetas=models.CharField(max_length=20)
    cirugias=models.TextField()
    fibrosis=models.TextField()
    costumbresA=models.TextField()
    deportesP=models.TextField()
    #Modo vida
    modoV=models.CharField(max_length=10)
    fuma=models.CharField(max_length=2)
    alcohol=models.CharField(max_length=2)
    calidadS=models.CharField(max_length=5)
    notasV=models.TextField()
    #Observaciones
    problemasT=models.TextField()
    #Grasa localizada
    abdomen=models.CharField(max_length=2)
    muslos=models.CharField(max_length=2)
    nalgas=models.CharField(max_length=2)
    espalda=models.CharField(max_length=2)
    piernas=models.CharField(max_length=2)
    brazos=models.CharField(max_length=2) 
    notasO=models.TextField()
    tratamientosR=models.TextField()
    tratamientosE=models.TextField()
    #Antecedentes personales
    dermatitis=models.CharField(max_length=2)
    cirugias1=models.CharField(max_length=2)
    cualesC=models.TextField()
    hemofilia=models.CharField(max_length=2)
    embarazo=models.CharField(max_length=2)
    cancer=models.CharField(max_length=2)
    hepatitis=models.CharField(max_length=2)
    diabetes=models.CharField(max_length=2)
    artritis=models.CharField(max_length=2)
    artrosis=models.CharField(max_length=2)
    escoliosis=models.CharField(max_length=2)
    fracturas=models.CharField(max_length=2)
    implantesM=models.CharField(max_length=2)
    hipertencion=models.CharField(max_length=2)
    herniasD=models.CharField(max_length=2)
    dondeHD=models.TextField()
    hiperlordosis=models.CharField(max_length=2)
    hipercifosis=models.CharField(max_length=2)
    problemasC=models.CharField(max_length=2)
    hipotension=models.CharField(max_length=2)
    osteoporosis=models.CharField(max_length=2)
    osteomielitis=models.CharField(max_length=2)
    comedones=models.CharField(max_length=2)
    pustulas=models.CharField(max_length=2)
    brotes=models.CharField(max_length=2)
    quistes=models.CharField(max_length=2)
    nudulos=models.CharField(max_length=2)
    zonasA=models.TextField()
    #Adiposidadl
    adiposidadL=models.CharField(max_length=2)
    adiposidadZ=models.CharField(max_length=2)
    adiposidadC=models.CharField(max_length=2)
    #Cicatrices o estrías
    cicatricesEL=models.CharField(max_length=2)
    cicatricesEZ=models.CharField(max_length=2)
    cicatricesET=models.CharField(max_length=2)
    #Flacidez
    flacidezL=models.CharField(max_length=2)
    flacidezZ=models.CharField(max_length=2)
    flacidezC=models.CharField(max_length=2)
    #Alt.vasculares
    altVascularesL=models.CharField(max_length=2)
    altVascularesZ=models.CharField(max_length=2)
    altVascularesT=models.CharField(max_length=2)
    #Celulitis
    celulitisL=models.CharField(max_length=2)
    celulitisZ=models.CharField(max_length=2)
    celulitisC=models.CharField(max_length=2)
    #Temperatura
    temperatura=models.CharField(max_length=8)
    #Alt.pigmentarias
    altpigmentariasAR=models.CharField(max_length=2)
    altpigmentariasAL=models.CharField(max_length=2)
    altpigmentariasAP=models.CharField(max_length=2)
    altpigmentariasAMR=models.CharField(max_length=2)
    altpigmentariasALV=models.CharField(max_length=2)
    altpigmentariasAPV=models.CharField(max_length=2)
    #Sensación
    sensacionLG=models.CharField(max_length=2)
    sensacionMG=models.CharField(max_length=2)
    sensacionMUG=models.CharField(max_length=2)
    sensacionLF=models.CharField(max_length=2)
    sensacionMF=models.CharField(max_length=2)
    sensacionMUF=models.CharField(max_length=2)
    sensacionPD=models.CharField(max_length=2)
    sensacionPI=models.CharField(max_length=2)
    retieneL=models.CharField(max_length=2)
    varices=models.CharField(max_length=2)
    arañitas=models.CharField(max_length=2)
    observaciones=models.TextField()
    
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
    

