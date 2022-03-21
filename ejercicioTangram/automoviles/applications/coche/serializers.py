from rest_framework import serializers
from .models import Coche
from applications.marca.serializers import MarcaSerializer
from applications.modelo.serializers import ModeloSerializer

class CocheSerializer(serializers.ModelSerializer):

    marca = MarcaSerializer()
    modelo = ModeloSerializer()

    class Meta:
        model = Coche
        fields = (
            'matricula',
            'fecha_creacion',
            'marca',
            'modelo',
        )

class CocheSerializerBase(serializers.ModelSerializer):

    class Meta:
        model = Coche
        fields = (
            'matricula',
            'fecha_creacion',
            'marca',
            'modelo',
        )