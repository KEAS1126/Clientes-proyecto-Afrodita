from django.shortcuts import render, redirect
from django.http import HttpResponse
from clientes.models import Clientes,EsteticoCorporal,ControlMedidas,EsteticoFacial

# Create your views here.

def saludo(request):
    return HttpResponse("Hola Universo")

def formularioCliente(request):
    return render(request,"crearCliente.html")

def crearCliente(request):
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
    return redirect("/cliente/")

def formularioCorporal(request,idCliente):
    cliente=Clientes.objects.filter(idCliente=idCliente).first()
    clientes={"cliente":cliente}
    return render(request,"crearCorporal.html",clientes)

def formularioControlMedidas(request,idCorporal):
    corporal=EsteticoCorporal.objects.filter(idCorporal=idCorporal).first()
    clientes={"corporal":corporal}
    return render(request,"crearControlMedidas.html",clientes)

def crearCorporal(request,idCliente):
    crearId=Clientes.objects.get(idCliente=idCliente)
    nombreECorporal=request.GET['nombreE']
    #Sufre problemas
    tensionACorporal=request.GET['tensionA']
    digestivoCorporal=request.GET['digestivo']
    circulacionCorporal=request.GET['circulacion']
    endocrinoCorporal=request.GET['endocrino']
    cardiacosCorporal=request.GET['cardiacos']
    otrosPCorporal=request.GET['otrosP']
    #Peso actual
    kilosCorporal=request.GET['kilos']
    tallaCorporal=request.GET['talla']
    alturaCorporal=request.GET['altura'] 
    masaCCorporal=request.GET['masaC']
    siluetasCorporal=request.GET['siluetas']
    cirugiasCorporal=request.GET['cirugias']
    fibrosisCorporal=request.GET['fibrosis']
    costumbresACorporal=request.GET['costumbresA']
    deportesPCorporal=request.GET['deportesP']
    #Modo vida
    modoVCorporal=request.GET['modoV']
    fumaCorporal=request.GET['fuma']
    alcoholCorporal=request.GET['alcohol']
    calidadSCorporal=request.GET['calidadS']
    notasVCorporal=request.GET['notasV']
    #Observaciones
    problemasTCorporal=request.GET['problemasT']
    #Grasa localizada
    abdomenCorporal=request.GET['abdomen']
    muslosCorporal=request.GET['muslos']
    nalgasCorporal=request.GET['nalgas']
    espaldaCorporal=request.GET['espalda']
    piernasCorporal=request.GET['piernas']
    brazosCorporal=request.GET['brazos']
    notasOCorporal=request.GET['notasO']
    tratamientosRCorporal=request.GET['tratamientosR']
    tratamientosECorporal=request.GET['tratamientosE']
    #Antecedentes personales
    dermatitisCorporal=request.GET['dermatitis']
    cirugias1Corporal=request.GET['cirugias1']
    cualesCCorporal=request.GET['cualesC']
    hemofiliaCorporal=request.GET['hemofilia']
    embarazoCorporal=request.GET['embarazo']
    cancerCorporal=request.GET['cancer']
    hepatitisCorporal=request.GET['hepatitis']
    diabetesCorporal=request.GET['diabetes']
    artitrisCorporal=request.GET['artritis']
    artrosisCorporal=request.GET['artrosis']
    escoliosisCorporal=request.GET['escoliosis']
    fracturasCorporal=request.GET['fracturas']
    implantesMCorporal=request.GET['implantesM']
    hipertensionCorporal=request.GET['hipertension']
    herniasDCorporal=request.GET['herniasD']
    dondeHDCorporal=request.GET['dondeHD']
    hiperlordosisCorporal=request.GET['hiperlordosis']
    hipercifosisCorporal=request.GET['hipercifosis']
    problemasCCorporal=request.GET['problemasC']
    hipotensionCorporal=request.GET['hipotension']
    osteoporosisCorporal=request.GET['osteoporosis']
    osteomielitisCorporal=request.GET['osteomielitis']
    comedonesCorporal=request.GET['comedones']
    pustulasCorporal=request.GET['pustulas']
    brotesCorporal=request.GET['brotes']
    quistesCorporal=request.GET['quistes']
    nodulosCorporal=request.GET['nodulos']
    zonasACorporal=request.GET['zonasA']
    
    #Adiposidad
    adiposidadLCorporal=request.GET['adiposidadL']
    adiposidadZCorporal=request.GET['adiposidadZ']
    adiposidadCCorporal=request.GET['adiposidadC']
    #Cicatrices o estrías
    cicatricesELCorporal=request.GET['cicatricesEL']
    cicatricesEZCorporal=request.GET['cicatricesEZ']
    cicatricesETCorporal=request.GET['cicatricesET']
    #Flacidez
    flacidezLCorporal=request.GET['flacidezL']
    flacidezZCorporal=request.GET['flacidezZ']
    flacidezCCorporal=request.GET['flacidezC']
    #Alt.vasculares
    altVascularesLCorporal=request.GET['altVascularesL']
    altVascularesZCorporal=request.GET['altVascularesZ']
    altVascularesTCorporal=request.GET['altVascularesT']
    #Celulitis
    celulitisLCorporal=request.GET['celulitisL']
    celulitisZCorporal=request.GET['celulitisZ']
    celulitisCCorporal=request.GET['celulitisC']
    #Temperatura
    temperaturaCorporal=request.GET['temperatura']
    #Alt.pigmentarias
    altpigmentariasARCorporal=request.GET['altpigmentariasAR']
    altpigmentariasALCorporal=request.GET['altpigmentariasAL']
    altpigmentariasAPCorporal=request.GET['altpigmentariasAP']
    altpigmentariasAMRCorporal=request.GET['altpigmentariasAMR']
    altpigmentariasALVCorporal=request.GET['altpigmentariasALV']
    altpigmentariasAPVCorporal=request.GET['altpigmentariasAPV']
    #Sensación
    sensacionLGCorporal=request.GET['sensacionLG']
    sensacionMGCorporal=request.GET['sensacionMG']
    sensacionMUGCorporal=request.GET['sensacionMUG']
    sensacionLFCorporal=request.GET['sensacionLF']
    sensacionMFCorporal=request.GET['sensacionMF']
    sensacionMUFCorporal=request.GET['sensacionMUF']
    sensacionPDCorporal=request.GET['sensacionPD']
    sensacionPICorporal=request.GET['sensacionPI']
    retieneLCorporal=request.GET['retieneL']
    varicesCorporal=request.GET['varices']
    aranitasCorporal=request.GET['aranitas']
    observacionesCorporal=request.GET['observaciones']

    corporal=EsteticoCorporal(nombreE=nombreECorporal,tensionA=tensionACorporal,digestivo=digestivoCorporal,circulacion=circulacionCorporal,endrocrino=endocrinoCorporal,cardiacos=cardiacosCorporal,otrosP=otrosPCorporal,kilos=kilosCorporal,talla=tallaCorporal,altura=alturaCorporal,masaC=masaCCorporal,siluetas=siluetasCorporal,cirugias=cirugiasCorporal,fibrosis=fibrosisCorporal,costumbresA=costumbresACorporal,deportesP=deportesPCorporal,modoV=modoVCorporal,fuma=fumaCorporal, alcohol=alcoholCorporal,calidadS=calidadSCorporal,notasV=notasVCorporal,problemasT=problemasTCorporal,abdomen=abdomenCorporal,muslos=muslosCorporal,nalgas=nalgasCorporal,espalda=espaldaCorporal,piernas=piernasCorporal,brazos=brazosCorporal,notasO=notasOCorporal,tratamientosR=tratamientosRCorporal,tratamientosE=tratamientosECorporal,dermatitis=dermatitisCorporal,cirugias1=cirugias1Corporal,
    cualesC=cualesCCorporal,hemofilia=hemofiliaCorporal,embarazo=embarazoCorporal,cancer=cancerCorporal,hepatitis=hepatitisCorporal,diabetes=diabetesCorporal,artritis=artitrisCorporal,artrosis=artrosisCorporal,escoliosis=escoliosisCorporal,fracturas=fracturasCorporal,implantesM=implantesMCorporal,hipertencion=hipertensionCorporal,
    herniasD=herniasDCorporal,dondeHD=dondeHDCorporal,hiperlordosis=hiperlordosisCorporal,hipercifosis=hipercifosisCorporal,
    problemasC=problemasCCorporal,
    hipotension=hipotensionCorporal,osteoporosis=osteoporosisCorporal,osteomielitis=osteomielitisCorporal,comedones=comedonesCorporal,pustulas=pustulasCorporal,brotes=brotesCorporal,quistes=quistesCorporal,nudulos=nodulosCorporal,zonasA=zonasACorporal,adiposidadL=adiposidadLCorporal,adiposidadZ=adiposidadZCorporal,adiposidadC=adiposidadCCorporal,cicatricesEL=cicatricesELCorporal,cicatricesEZ=cicatricesEZCorporal,cicatricesET=cicatricesETCorporal,flacidezL=flacidezLCorporal,flacidezZ=flacidezZCorporal,flacidezC=flacidezCCorporal,altVascularesL=altVascularesLCorporal,altVascularesZ=altVascularesZCorporal,
    altVascularesT=altVascularesTCorporal,celulitisL=celulitisLCorporal,celulitisZ=celulitisZCorporal,
    celulitisC=celulitisCCorporal,temperatura=temperaturaCorporal,altpigmentariasAR=altpigmentariasARCorporal,altpigmentariasAL=altpigmentariasALCorporal,altpigmentariasAP=altpigmentariasAPCorporal,altpigmentariasAMR=altpigmentariasAMRCorporal,altpigmentariasALV=altpigmentariasALVCorporal,altpigmentariasAPV=altpigmentariasAPVCorporal,sensacionLG=sensacionLGCorporal,sensacionMG=sensacionMGCorporal,sensacionMUG=sensacionMUGCorporal,sensacionLF=sensacionLFCorporal,sensacionMF=sensacionMFCorporal,sensacionMUF=sensacionMUFCorporal,sensacionPD=sensacionPDCorporal,sensacionPI=sensacionPICorporal,retieneL=retieneLCorporal,varices=varicesCorporal,arañitas=aranitasCorporal,observaciones=observacionesCorporal,idCliente=crearId
    )
    corporal.save()
    return redirect("/cliente/")

def crearControMedidas(request,idCorporal):
    crearIdC=EsteticoCorporal.objects.get(idCorporal=idCorporal)
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
    return redirect("/cliente/")

def formularioFacial(request,idCliente):
    mostrar=Clientes.objects.filter(idCliente=idCliente).first()
    clientes={"mostrar":mostrar}
    return render(request,"crearFacial.html",clientes)

def crearFacial(request,idCliente):
    crearId=Clientes.objects.get(idCliente=idCliente)
    nombreEFacial=request.GET['nombreE']
    #Factores agravantes
    tratamientoMFacial=request.GET['tratamientoM']
    cualTMFacial=request.GET['cualTM']
    sustitucionHFacial=request.GET['sustitucionH']
    tomaAFacial=request.GET['tomaA']
    drogasFacial=request.GET['drogas']
    alimentosPFacial=request.GET['alimentosP']
    alimentosRFacial=request.GET['alimentosR']
    fumaFacial=request.GET['fuma']
    tomaLFacial=request.GET['tomaL']
    protegeSFacial=request.GET['protegeS']
    duermeBFacial=request.GET['duermeB']
    menopausiaFacial=request.GET['menopausia']
    medicamentosOTFacial=request.GET['medicamentosOT']
    cualesOTFacial=request.GET['cualesOT']
    padeceEFacial=request.GET['padeceE']
    cancerPFacial=request.GET['cancerP']
    asmaFacial=request.GET['asma']
    lupusFacial=request.GET['lupus']
    herpesFacial=request.GET['herpes']
    hepatitisFacial=request.GET['hepatitis']
    epilepsiaFacial=request.GET['epilepsia']
    dolorCFacial=request.GET['dolorC']
    ampollasFFacial=request.GET['ampollasF']
    tiroidesFacial=request.GET['tiroides']
    problemasCFacial=request.GET['problemasC']
    psicológicosFacial=request.GET['psicológicos']
    urinariosFacial=request.GET['urinarios']
    nasalesFacial=request.GET['nasales']
    digestivosFacial=request.GET['digestivos']
    #Está utilizando o uso
    alfahidroxiacidosFacial=request.GET['alfahidroxiacidos']
    retinAFacial=request.GET['retinA']
    differinFacial=request.GET['differin']
    accutaneFacial=request.GET['accutane']
    motivoCFacial=request.GET['motivoC']
    productoCMFacial=request.GET['productoCM']
    #Analisis de piel
    normalFacial=request.GET['normal']
    gruesaFacial=request.GET['gruesa']
    asperaFacial=request.GET['aspera']
    suaveFacial=request.GET['suave']
    normal1Facial=request.GET['normal1']
    cerradoFacial=request.GET['cerrado']
    dilatadoFacial=request.GET['dilatado']
    #Brillo
    zonasMFacial=request.GET['zonasM']
    zonasBFacial=request.GET['zonasB']
    #Grado de hidratación
    normal2Facial=request.GET['normal2']
    deshidratadaFacial=request.GET['deshidratada']
    hiperdeshidratadaFacial=request.GET['hiperdeshidratada']
    #Fototipo de piel
    fototipoPFacial=request.GET['fototipoP']
    #Alteraciones del envejecimiento
    lineasFFacial=request.GET['lineasF']
    profundasFacial=request.GET['profundas']
    flacidezFacial=request.GET['flacidez']
    parpadosFacial=request.GET['parpados']
    cuelloFacial=request.GET['cuello']
    nasogenianosFacial=request.GET['nasogenianos']
    labiosFacial=request.GET['labios']
    #Acné(desde cuándo)
    comedonesFacial=request.GET['comedones']
    miliasFacial=request.GET['milias']
    quistesFacial=request.GET['quistes']
    #Pigmentación
    melasmaFacial=request.GET['melasma']
    hipercromiaFacial=request.GET['hipercromia']
    edemaFacial=request.GET['edema']
    grasaFacial=request.GET['grasa']
    #Cuidados que realiza diariamente
    rutinaHFacial=request.GET['rutinaH']
    cuidadosHFacial=request.GET['cuidadosH']
    mensualesFacial=request.GET['mensuales']
    productoHFacial=request.GET['productoH']

    facial=EsteticoFacial(nombreE=nombreEFacial,tratamientoM=tratamientoMFacial,cualTM=cualTMFacial,sustitucionH=sustitucionHFacial,tomaA=tomaAFacial,drogas=drogasFacial,alimentosP=alimentosPFacial,alimentosR=alimentosRFacial,fuma=fumaFacial,tomaL=tomaLFacial,protegeS=protegeSFacial,duermeB=duermeBFacial,menopausia=menopausiaFacial,medicamentosOT=medicamentosOTFacial,cualesOT=cualesOTFacial,padeceE=padeceEFacial,cancerP=cancerPFacial,asma=asmaFacial,lupus=lupusFacial,herpes=herpesFacial,hepatitis=hepatitisFacial,epilepsias=epilepsiaFacial,dolorC=dolorCFacial,ampollasF=ampollasFFacial,tiroides=tiroidesFacial,problemasC=problemasCFacial,psicologicos=psicológicosFacial,urinarios=urinariosFacial,nasales=nasalesFacial,digestivos=digestivosFacial,alfahidroxiacidos=alfahidroxiacidosFacial,retinA=retinAFacial,differin=differinFacial,accutane=accutaneFacial,motivoC=motivoCFacial,productoCM=productoCMFacial,normal=normalFacial,gruesa=gruesaFacial,aspera=asperaFacial,suave=suaveFacial,normal1=normal1Facial,cerrado=cerradoFacial,dilatado=dilatadoFacial,zonasM=zonasMFacial,zonasB=zonasBFacial,normal2=normal2Facial,deshidratada=deshidratadaFacial,hiperdeshidratada=hiperdeshidratadaFacial,fototipoP=fototipoPFacial,lineasF=lineasFFacial,profundas=profundasFacial,flacidez=flacidezFacial,parpados=parpadosFacial,cuello=cuelloFacial,nasogenianos=nasalesFacial,labios=labiosFacial,comedones=comedonesFacial,milias=miliasFacial,quistes=quistesFacial,melasma=melasmaFacial,hipercromia=hipercromiaFacial,edema=edemaFacial,grasa=grasaFacial,rutinasH=rutinaHFacial,cuidadosH=cuidadosHFacial,mensuales=mensualesFacial,productoH=productoHFacial,idCliente=crearId)
    facial.save()
    return redirect("/cliente/")

def cliente(request):
    cliente=Clientes.objects.filter()
    clientes={"cliente":cliente}
    return render(request,"clientes.html",clientes)

def editar(request, idCliente):
    mostrar=Clientes.objects.filter(idCliente=idCliente).first()
    clientes={"mostrar":mostrar}
    return render(request,"editarCliente.html",clientes)
    
def actualizar(request, idCliente):
    nombreCliente=request.GET['nombre']
    documentoCliente=request.GET['documento']
    sexoCliente=request.GET['sexo']
    telefonoCliente=request.GET['telefono']
    direccionCliente=request.GET['direccion']
    correoCliente=request.GET['correo']
    fechaNacimientoCliente=request.GET['fechaNacimiento']
    estadoCivilCliente=request.GET['estadoCivil']
    numeroHijosCliente=request.GET['numeroHijos']
    actualizar=Clientes.objects.get(idCliente=idCliente)
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
    return redirect("/cliente/")

def verDetalleCliente(request, idCliente):
    mostrar=Clientes.objects.filter(idCliente=idCliente).first()
    corporal=EsteticoCorporal.objects.filter(idCliente=idCliente) 
    facial=EsteticoFacial.objects.filter(idCliente=idCliente) 
    clientes={"mostrar":mostrar,"corporal":corporal,"facial":facial}
    return render(request,"VerDetalleCliente.html",clientes)

def verDetalleCorporal(request, idCorporal):
    mostrar=EsteticoCorporal.objects.filter(idCorporal=idCorporal).first()
    medidas=ControlMedidas.objects.filter(idCorporal=idCorporal)
    corporal={"mostrar":mostrar,"medidas":medidas}
    return render(request,"VerDetalleCorporal.html",corporal)

def verDetalleFacial(request, idFacial):
    mostrar=EsteticoFacial.objects.filter(idFacial=idFacial).first()
    facial={"mostrar":mostrar}
    return render(request,"VerDetalleFacial.html",facial)

