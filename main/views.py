from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
import json
from django.shortcuts import redirect

from .models import Region, Asesor, Cliente, Contrata



# Create your views here.
def mostrarContacto(request):
    context = {}
    return render(request,'main/contacto/contacto.html',context)

def mostrarAsesores(request, id_region):
    asesores = Asesor.objects.filter(region = id_region)
    regiones = Region.objects.filter(activo=True)
    context = {'asesores':asesores,'regiones':regiones,"oRegion":id_region,}
    return render(request,'main/asesores/asesores.html',context)

def mostrarAsesor(request, id):
    asesor = Asesor.objects.get(id= id )
    context = {'asesor':asesor,}
    return render(request,'main/asesor/asesor.html',context)

def mostrarIndex(request):
    context = {}
    return render(request,'main/index/index.html',context)

def mostrarNosotros(request):
    context = {}
    return render(request,'main/nosotros/nosotros.html',context)

def mostrarServicios(request):
    context = {}
    return render(request,'main/servicios/servicios.html',context)

def mostrarPago(request, id):
    asesor = Asesor.objects.get(id= id )
    context = {'asesor':asesor,}
    return render(request,'pago/pago.html',context)


def registrarAsesor(request):
    regiones = Region.objects.filter(activo=True)
    context = {'regiones':regiones,}
    return render(request,'asesor/registrar.html',context)

def registrarRegion(request):
    context = {}
    return render(request,'region/registrar.html',context)

def listarContrata(request):
    contratas = Contrata.objects.all()
    context = {'contratas': contratas,}
    return render(request,'contrata/listar.html',context)
    
def registarAsesorAPI(request):
    if request.method == 'POST':
        data = request.POST, request.FILES
        # print(data[0]['nombre'])
        region = Region.objects.get(id=data[0]['region'])
        asesor = Asesor(
            nombre = data[0]['nombre'],
            tipo_documento =data[0]['tipo_documento'],
            documento = data[0]['documento'],
            telefono = data[0]['telefono'],
            correo = data[0]['correo'],
            funcion = data[0]['funcion'],
            precio = data[0]['precio'],
            region = region,
            foto = data[1]['foto'],
            
            )
        asesor.save()
        
        return redirect('/asesor/registrar/')

def registarRegionAPI(request):
    if request.method == 'POST':
        data = request.POST, request.FILES
        # print(data[0]['nombre'])
        region = Region(
            nombre = data[0]['nombre'],
            
            )
        region.save()
        
        return redirect('/region/registrar/')

def registrarContrataAPI(request,id):
    if request.method=='POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        cliente = Cliente()
        cliente.nombre = body['nombre']
        cliente.apellido = body['apellido']
        cliente.telefono = body['telefono']
        cliente.direccion = body['direccion']
        cliente.save()

        asesor = Asesor.objects.get(id=id)

        contrata = Contrata()
        contrata.asunto = body['asunto']
        contrata.asesor = asesor
        contrata.cliente = cliente
        
        contrata.save()
        
    return HttpResponse(json.dumps("respuesta"), content_type='application/json')