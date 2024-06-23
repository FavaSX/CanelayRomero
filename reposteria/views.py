from django.shortcuts import render
from .models import Torta, Pan_pascua, Coctel

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
    return render(request, 'reposteria/contacto.html')
def iniciar_sesion(request):
    return render(request, 'reposteria/iniciar_sesion.html')
def registrarse(request):
    return render(request, 'reposteria/registrarse.html')
def sobre_nosotros(request):
    return render(request, 'reposteria/sobre_nosotros.html')