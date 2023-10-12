from django import forms
from tienda.models import Contacto


class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        
        fields = '__all__'
        