from .models import Perfil
from .serializers import UsuarioSerializer, PerfilSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from drf_yasg.utils import swagger_auto_schema
from ..autenticacao.models import Usuario


# class UsuarioViewsets(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     http_method_names = ["post", "get", "patch", "delete"]
#     lookup_field = "id"
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     @action(detail=False, methods=["get"], url_path="funcao")
#     def filtro(self, request, *args, **kwargs):
#         queryset = self.get_queryset().filter(perfil=request.data["funcao"])
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)


class UsuariosView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    http_method_names = ['get', 'delete']
    
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
