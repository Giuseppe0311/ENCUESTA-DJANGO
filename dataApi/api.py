from .models import *
from rest_framework import viewsets, permissions
from .serializers import *


class Perfilviewset(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PerfilSerilizers


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UsuarioSerializes


class PsicosisViewSet(viewsets.ModelViewSet):
    queryset = Psicosis.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PsicosisSerializer


class EpilepsiaViewSet(viewsets.ModelViewSet):
    queryset = Epilepsia.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EpilepsiaSerializer


class EncuestasViewSet(viewsets.ModelViewSet):
    queryset = Encuestas.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EncuestasSerializer


class AlcoholismoViewSet(viewsets.ModelViewSet):
    queryset = Alcoholismo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AlcoholismoSerializer


class AnsiedadDepresionViewSet(viewsets.ModelViewSet):
    queryset = Ansiedaddepresion.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AnsiedadDepresion


class DatosPersonalesViewSet(viewsets.ModelViewSet):
    queryset = Datospersonales.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DatosPersonalesSerializer
