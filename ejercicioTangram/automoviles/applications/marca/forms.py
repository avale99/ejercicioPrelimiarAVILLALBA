from django import forms

from .models import Marca

class MarcaForm(forms.ModelForm):
    
    class Meta:
        model = Marca
        fields = (
            'nombre',
            'fecha_fundacion',
            'telefono_atencion',
        )
        widgets = {
            'fecha_fundacion': forms.DateInput(
                attrs= {
                    'placeholder': 'Dia/Mes/Año',
                }
            )
        }