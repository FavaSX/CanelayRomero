from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'reposteria/home.html')
def contacto(request):
    return render(request, 'reposteria/contacto.html')
def iniciar_sesion(request):
    return render(request, 'reposteria/iniciar_sesion.html')
def registrarse(request):
    return render(request, 'reposteria/registrarse.html')
def sobre_nosotros(request):
    return render(request, 'reposteria/sobre_nosotros.html')