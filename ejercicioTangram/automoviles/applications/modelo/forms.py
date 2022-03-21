from django import forms

from .models import Modelo

class ModeloForm(forms.ModelForm):
    
    class Meta:
        model = Modelo
        fields = (
            'nombre',
            'carroceria',
            #'marca',
        )
        widgets = {
            'carroceria': forms.Select(),
            #'marca': forms.Select(),
        }