from rest_framework import serializers
from .models import FisicoQuimico


class FisicoQuimicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = FisicoQuimico
        fields = "__all__"
