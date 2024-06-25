from django.urls import path
from django.contrib.auth.decorators import user_passes_test
from .views import (
    home, contacto, login, registro, sobre_nosotros, 
    agregar_torta, agregar_coctel, agregar_pan_pascua, 
    listar_productos, modificar_producto, eliminar_producto
)

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('sobre_nosotros/', sobre_nosotros, name="sobre_nosotros"),
    path('agregar-torta/', user_passes_test(lambda u: u.is_superuser)(agregar_torta), name="agregar_torta"),
    path('agregar-coctel/', user_passes_test(lambda u: u.is_superuser)(agregar_coctel), name="agregar_coctel"),
    path('agregar-pan_pascua/', user_passes_test(lambda u: u.is_superuser)(agregar_pan_pascua), name="agregar_pan_pascua"),
    path('listar-productos/', user_passes_test(lambda u: u.is_superuser)(listar_productos), name="listar_productos"),
    path('modificar-producto/<str:tipo>/<int:id>/', user_passes_test(lambda u: u.is_superuser)(modificar_producto), name="modificar_producto"),
    path('eliminar-producto/<str:tipo>/<int:id>/', user_passes_test(lambda u: u.is_superuser)(eliminar_producto), name="eliminar_producto"),
]
