from django.contrib import admin
from .models import Modelo

class ModeloAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'carroceria',
        #'marca',
    )

    #
    search_fields = ('nombre',)
    list_filter = ('carroceria',)


admin.site.register(Modelo, ModeloAdmin)

