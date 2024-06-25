from django import forms
from .models import Contacto, Torta, Pan_pascua, Coctel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
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
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username', "first_name", "last_name", "email", "password1", "password2"]