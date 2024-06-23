from django.contrib import admin
from .models import Torta, Pan_pascua, Coctel, Contacto
# Register your models here.

class TortaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion", "precio"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    
class CoctelAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion", "precio"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    
class Pan_pascuaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion", "precio"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    
admin.site.register(Torta, TortaAdmin)

admin.site.register(Pan_pascua, Pan_pascuaAdmin)

admin.site.register(Coctel, CoctelAdmin)

admin.site.register(Contacto)