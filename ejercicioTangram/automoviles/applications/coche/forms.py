from django import forms

from .models import Coche

class CocheForm(forms.ModelForm):
    
    class Meta:
        model = Coche
        fields = (
            'matricula',
            'fecha_creacion',
            'marca',
            'modelo'
        )
        widgets = {
            'modelos': forms.Select(),
            'marca': forms.Select(),
            'fecha_creacion': forms.DateInput(
                attrs= {
                    'placeholder': 'Dia/Mes/Año',
                }
            )
        }
