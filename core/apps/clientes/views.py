from .models import Cliente
from .serializers import ClienteSerializers
from rest_framework import viewsets, status
from rest_framework.response import Response


class ClienteViewsets(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers
    http_method_names = ["post", "get", "patch", "delete"]
    lookup_field = "id"
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
