from django.db import models
from .managers import CocheManager

class Coche(models.Model):
    matricula = models.CharField('Matricula', max_length=7, unique=True)
    fecha_creacion = models.DateField('Fecha Creacion')
    modelo = models.ForeignKey('modelo.Modelo', verbose_name=("Modelo"), on_delete=models.SET_NULL, null=True)
    marca = models.ForeignKey('marca.Marca', verbose_name=("Marca"), on_delete=models.SET_NULL, null=True)

    MARCAS_COCHES=()

    objects = CocheManager()

    class Meta:
        verbose_name = 'Coche'
        verbose_name_plural = 'Coches'
        ordering = ['matricula']

    def __str__(self):
        return self.matricula

    #SHELL, Coche.objects.all()[X].dictionary()
    def dictionary(self):
        self.MARCAS_COCHES = (
            (self.marca.nombre, self.matricula)
            )
        return self.MARCAS_COCHES
