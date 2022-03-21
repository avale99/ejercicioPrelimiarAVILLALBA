from datetime import datetime
from django.db import models
from django.db.models import Q

class CocheManager(models.Manager):
    """ Managers para modelo coche """

    def listar_coches_kword(self, kword):
        lista = self.filter(
            Q(marca__nombre__icontains=kword) | Q(matricula__icontains=kword) | Q(modelo__nombre__icontains=kword),                
        )
        return lista

    def listar_coches_ltfecha(self, kword):
        lista = self.filter(
            fecha_creacion__lte = kword
        )
        return lista