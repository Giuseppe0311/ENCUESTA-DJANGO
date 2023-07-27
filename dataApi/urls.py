from rest_framework import routers
from .api import *
from django.urls import path, include

router = routers.DefaultRouter()
router.register('api/perfiles', Perfilviewset, basename='perfil')
router.register('api/usuarios', UsuarioViewSet, basename='usuario')
router.register('api/psicosis', PsicosisViewSet, basename='psicosis')
router.register('api/epilepsia', EpilepsiaViewSet, basename='epilepsia')
router.register('api/encuestas', EncuestasViewSet, basename='encuestas')
router.register('api/alcoholismo', AlcoholismoViewSet, basename='alcoholismo')
router.register('api/ansiedad', AnsiedadDepresionViewSet, basename='ansiedad')
router.register('api/datospersonales', DatosPersonalesViewSet,
                basename='datospersonales')
urlpatterns = [
    path('', include(router.urls)),
]
