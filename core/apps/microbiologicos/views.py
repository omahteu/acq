from .models import Microbiologico
from .serializers import MicrobiologicoSerializers
from rest_framework import viewsets, status
from rest_framework.response import Response


class MicrobiologicoViewsets(viewsets.ModelViewSet):
    queryset = Microbiologico.objects.all()
    serializer_class = MicrobiologicoSerializers
    http_method_names = ["post", "get", "patch", "delete"]
    lookup_field = "id"
