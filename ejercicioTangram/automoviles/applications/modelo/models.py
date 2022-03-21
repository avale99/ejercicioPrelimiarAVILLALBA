from django.db import models
from .managers import ModeloManager
from django.template.defaulttags import register

class Modelo(models.Model):
    CARROCERIA_CHOICES=(
            ('0', 'Sedán'),
            ('1', 'Familiar'),
            ('2', 'Coupé'),
            ('3', 'Todoterreno'),
            ('4', 'Descapotable'),
            ('5', 'SUV'),
        )

    nombre = models.CharField('Modelo', max_length=50, unique=True)
    carroceria = models.CharField('Carroceria', max_length=1, choices=CARROCERIA_CHOICES)
    #marca = models.ForeignKey('marca.Marca', verbose_name=("Marca"), on_delete=models.SET_NULL, blank=True, null=True)
    
    objects = ModeloManager()

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'
        ordering = ['id']

    def __str__(self):
        return self.nombre

    @register.filter
    def get_carroceria(self, key):
        return self[int(key)]
