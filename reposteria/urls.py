from django.urls import path
from .views import home, contacto, iniciar_sesion, registrarse, sobre_nosotros

urlpatterns = [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('iniciar_sesion', iniciar_sesion, name="iniciar_sesion"),
    path('registrarse', registrarse, name="registrarse"),
    path('sobre_nosotros', sobre_nosotros, name="sobre_nosotros"),
]
