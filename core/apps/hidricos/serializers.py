from rest_framework import serializers
from .models import Hidricos


class HidricosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hidricos
        fields = "__all__"
    
    # def validate(self, attrs):
    #     return super().validate(attrs)
