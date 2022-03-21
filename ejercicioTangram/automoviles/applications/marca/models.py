from django.db import models
from .managers import MarcaManager

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField('Marca', max_length=50, unique=True)
    fecha_fundacion = models.DateField('Fundacion')
    telefono_atencion = models.IntegerField('Telefono', unique=True)

    objects = MarcaManager()

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['id']

    def __str__(self):
        return self.nombre
