from .models import Hidricos
from .serializers import HidricosSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend


class HidricosViewsets(viewsets.ModelViewSet):
    queryset = Hidricos.objects.all()
    serializer_class = HidricosSerializer
    http_method_names = ["post", "get", "patch", "delete"]
    lookup_field = "id"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'estado']
    
    @action(detail=False, methods=["get"], url_path="nome_estado")
    def nome_estado(self, request, *args, **kwargs):
        
        queryset = self.get_queryset().filter(nome=request.data["nome_estado"])
        
        if queryset:
            serializer = self.get_serializer(queryset, many=True)
            
        else:
            queryset = self.get_queryset().filter(estado=request.data["nome_estado"])
            serializer = self.get_serializer(queryset, many=True)
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        return Response(serializer.data)
