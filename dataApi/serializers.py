from rest_framework import serializers
from .models import *

# this serializer is already with url


class PerfilSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'


class UsuarioSerializes(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class PsicosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psicosis
        fields = '__all__'


class EpilepsiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epilepsia
        fields = '__all__'


class EncuestasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuestas
        fields = '__all__'


class AlcoholismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alcoholismo
        fields = '__all__'


class AnsiedadDepresion(serializers.ModelSerializer):
    class Meta:
        model = Ansiedaddepresion
        fields = '__all__'


class DatosPersonalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datospersonales
        fields = '__all__'
