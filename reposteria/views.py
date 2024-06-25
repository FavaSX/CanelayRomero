from django.shortcuts import render, redirect, get_object_or_404
from .models import Torta, Pan_pascua, Coctel
from .forms import ContactoForm, TortaForm, CoctelForm, Pan_pascuaForm, CustomUserCreationForm
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import user_passes_test
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
def login(request):
    return render(request, 'registration/login.html')
def registro(request):
    data={
        'form':CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario= CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            auth_login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"]= formulario
    return render(request, 'registration/registro.html', data)
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
            messages.success(request, "Torta guardado con exito")
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
            messages.success(request, "Coctel guardado con exito")
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
            messages.success(request, "Pan de pascua guardado con exito")
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

def modificar_producto(request, tipo, id):
    if tipo == "torta":
        producto = get_object_or_404(Torta, id=id)
        form_class = TortaForm
    elif tipo == "coctel":
        producto = get_object_or_404(Coctel, id=id)
        form_class = CoctelForm
    elif tipo == "pan_pascua":
        producto = get_object_or_404(Pan_pascua, id=id)
        form_class = Pan_pascuaForm
    else:
        raise Http404("Producto no encontrado")

    data = {
        'form': form_class(instance=producto),
        'tipo': tipo
    }

    if request.method == 'POST':
        formulario = form_class(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado con Exito")
            return redirect(to="listar_productos")
        data["form"] = formulario

    return render(request, 'reposteria/producto/modificar.html', data)

def eliminar_producto(request, tipo, id):
    if tipo == "torta":
        producto = get_object_or_404(Torta, id=id)
    elif tipo == "coctel":
        producto = get_object_or_404(Coctel, id=id)
    elif tipo == "pan_pascua":
        producto = get_object_or_404(Pan_pascua, id=id)
    else:
        raise Http404("Producto no encontrado")

    if request.method == "POST":
        producto.delete()
        messages.success(request, "Eliminado con exito")
        return redirect(to="listar_productos")

    return redirect(to="listar_productos")

def es_superuser(user):
    return user.is_superuser