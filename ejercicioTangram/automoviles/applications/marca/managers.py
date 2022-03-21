from django.db import models
from django.db.models import Q

class MarcaManager(models.Manager):
    """ Managers para modelo marca """

    def listar_marcas(self, kword):
       #return self.all()
        lista = self.filter(
            nombre__icontains = kword
        )
        return lista
