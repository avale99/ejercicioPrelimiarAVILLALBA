from django.contrib import admin
from .models import Marca

class MarcaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'fecha_fundacion',
        'telefono_atencion',
    )

    #
    search_fields = ('nombre',)


admin.site.register(Marca, MarcaAdmin)