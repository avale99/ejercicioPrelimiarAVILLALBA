from django.db import models
from django.db.models import Q

class ModeloManager(models.Manager):
    """ Managers para modelo modelo """

    def listar_modelos(self, kword):
        #return self.all()
        lista = self.filter(
            nombre__icontains = kword
        )
        return lista