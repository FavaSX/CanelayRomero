from django import forms
from .models import Contacto, Torta, Pan_pascua, Coctel
class ContactoForm(forms.ModelForm):
    
    class Meta:
        model= Contacto
        fields= '__all__'
    
class TortaForm(forms.ModelForm):
    class Meta:
        model=Torta
        fields='__all__'
        
class CoctelForm(forms.ModelForm):
    class Meta:
        model=Coctel
        fields='__all__'

class Pan_pascuaForm(forms.ModelForm):
    class Meta:
        model=Pan_pascua
        fields='__all__'