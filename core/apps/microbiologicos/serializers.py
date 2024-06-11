from rest_framework import serializers
from .models import Microbiologico


class MicrobiologicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Microbiologico
        fields = "__all__"
