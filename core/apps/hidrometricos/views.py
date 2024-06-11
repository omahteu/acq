from .models import Hidrometrico
from .serializers import HidrometricoSerializers
from rest_framework import viewsets, status
from rest_framework.response import Response


class HidrometricoViewSets(viewsets.ModelViewSet):
    queryset = Hidrometrico.objects.all()
    serializer_class = HidrometricoSerializers
    http_method_names = ["post", "get", "patch", "delete"]
    lookup_field = "id"
