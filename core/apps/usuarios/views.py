from .models import Perfil
from .serializers import UsuarioSerializer, PerfilSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from drf_yasg.utils import swagger_auto_schema
from ..autenticacao.models import Usuario
from django_filters.rest_framework import DjangoFilterBackend


class UsuariosView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    http_method_names = ['get', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['perfis', 'nome']
    
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.active = False
        user.save()
        return Response(status=status.HTTP_200_OK)


class CustomParametrosView(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.active = False
        obj.save()
        return Response(status=status.HTTP_200_OK)


class PerfilView(CustomParametrosView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
