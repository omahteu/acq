from rest_framework import serializers
from .models import Localidade


class LocalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localidade
        fields = "__all__"
