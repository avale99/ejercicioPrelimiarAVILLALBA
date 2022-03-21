from rest_framework import serializers
from .models import Modelo

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = (
            'id',
            'nombre',
            'carroceria',
        )