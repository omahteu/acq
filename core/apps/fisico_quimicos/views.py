from rest_framework import viewsets
from .models import FisicoQuimico
from .serializers import FisicoQuimicoSerializers


class FisicoQuimicoViewSets(viewsets.ModelViewSet):
    queryset = FisicoQuimico.objects.all()
    serializer_class = FisicoQuimicoSerializers
    http_method_names = ["post", "get", "patch", "delete"]
    lookup_field = "id"
