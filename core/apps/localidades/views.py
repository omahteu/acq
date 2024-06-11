from .models import Localidade
from .serializers import LocalidadeSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class LocalidadeViewsets(viewsets.ModelViewSet):
    queryset = Localidade.objects.all()
    serializer_class = LocalidadeSerializer
    http_method_names = ["post", "get", "patch", "delete"]
    lookup_field = "id"
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
