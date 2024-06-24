from django.urls import path
from .views import home, contacto, iniciar_sesion, registrarse, sobre_nosotros, agregar_torta, agregar_coctel, agregar_pan_pascua, listar_productos

urlpatterns = [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('iniciar_sesion', iniciar_sesion, name="iniciar_sesion"),
    path('registrarse', registrarse, name="registrarse"),
    path('sobre_nosotros', sobre_nosotros, name="sobre_nosotros"),
    path('agregar-torta', agregar_torta, name="agregar_torta"),
    path('agregar-coctel', agregar_coctel, name="agregar_coctel"),
    path('agregar-pan_pascua', agregar_pan_pascua, name="agregar_pan_pascua"),
    path('listar-productos', listar_productos, name="listar_productos"),
]
