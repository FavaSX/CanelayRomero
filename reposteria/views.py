from django.shortcuts import render
from .models import Torta, Pan_pascua, Coctel
from .forms import ContactoForm, TortaForm, CoctelForm, Pan_pascuaForm

# Create your views here.
def home(request):
    tortas = Torta.objects.all()
    tortas_slide1 = tortas[0:5]
    tortas_slide2 = tortas[5:10]
    tortas_slide3 = tortas[10:15]
    pan_pascuas = Pan_pascua.objects.all()
    coctels = Coctel.objects.all()
    data={
        'tortas_slide1':tortas_slide1,
        'tortas_slide2':tortas_slide2,
        'tortas_slide3':tortas_slide3,
        'tortas': tortas,
        'pan_pascuas': pan_pascuas,
        'coctels': coctels
    }
    return render(request, 'reposteria/home.html', data)
def contacto(request):
    data={
        'form': ContactoForm()
    }
    if request.method=='POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Solicitud enviada correctamente"
        else:
            data["form"]=formulario
    return render(request, 'reposteria/contacto.html', data)
def iniciar_sesion(request):
    return render(request, 'reposteria/iniciar_sesion.html')
def registrarse(request):
    return render(request, 'reposteria/registrarse.html')
def sobre_nosotros(request):
    return render(request, 'reposteria/sobre_nosotros.html')
def agregar_torta(request):
    data = {
        'form': TortaForm()
        }
    if request.method == 'POST':
        formulario = TortaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Torta guardada correctamente"
        else:
            data["form"] = formulario
    return render(request, 'reposteria/producto/agregar_torta.html', data)
def agregar_coctel(request):
    data = {
        'form': CoctelForm()
        }
    if request.method == 'POST':
        formulario = CoctelForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Coctel guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'reposteria/producto/agregar_coctel.html', data)
def agregar_pan_pascua(request):
    data = {
        'form': TortaForm()
        }
    if request.method == 'POST':
        formulario = Pan_pascuaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Pan de pascua guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'reposteria/producto/agregar_pan_pascua.html', data)

def listar_productos(request):
    tortas= Torta.objects.all()
    coctels= Coctel.objects.all()
    pan_pascuas= Pan_pascua.objects.all()
    data={
        'tortas':tortas,
        'coctels':coctels,
        'pan_pascuas':pan_pascuas
    }
    return render(request, 'reposteria/producto/listar.html', data)