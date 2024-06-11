from .models import Cliente
from rest_framework import serializers
from .tools.validacao_cnpj import cnpj
from .tools.validacao_telefone import telefone


class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

    def validate_cnpj(self, value):
        print(value)
        if not cnpj(value):
            raise serializers.ValidationError("CNPJ inválido.")
        return value

    def validate_telefone(self, value):
        if not telefone(value):
            raise serializers.ValidationError("Número de telefone inválido.")
        return value

