from .models import Hidrometrico
from rest_framework import serializers


class HidrometricoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hidrometrico
        fields = "__all__"
