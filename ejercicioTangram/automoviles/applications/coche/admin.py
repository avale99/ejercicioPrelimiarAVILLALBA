from django.contrib import admin
from .models import Coche

class CocheAdmin(admin.ModelAdmin):
    list_display = (
        'matricula',
        'fecha_creacion',
        'modelo',
        'marca',
    )

    search_fields = ('matricula',)
    #
    list_filter = ('marca', 'modelo', 'fecha_creacion',)


admin.site.register(Coche, CocheAdmin)
