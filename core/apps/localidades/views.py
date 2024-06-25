from .models import Localidade
from .serializers import LocalidadeSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class LocalidadeViewsets(viewsets.ModelViewSet):
    queryset = Localidade.objects.all()
    serializer_class = LocalidadeSerializer
    http_method_names = ["post", "get", "patch", "delete"]
    lookup_field = "id"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'cidade']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
