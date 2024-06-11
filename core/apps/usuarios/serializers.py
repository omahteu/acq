from rest_framework import serializers
from .models import Perfil
from django.contrib.auth.hashers import make_password
from .tools.validacao_cpf import cpf
from ..autenticacao.models import Usuario

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password', 'perfil', 'cpf', 'estado', 'cidade', 'bacia_responsavel', 'cliente']
#         extra_kwargs = {'password': {'write_only': True}}

#     def validate(self, attrs):
#         attrs['password'] = make_password(attrs['password'])

#         return super().validate(attrs)

#     def validate_cpf(self, value):
#         if not cpf(value):
#             raise serializers.ValidationError("CPF inválido.")

#         return value

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
        depth = 1


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'
