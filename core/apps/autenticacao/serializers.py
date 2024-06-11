from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.password_validation import validate_password
from drf_yasg.utils import swagger_serializer_method

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.exceptions import (
    AuthenticationFailed,
    TokenError,
)
from rest_framework_simplejwt.tokens import RefreshToken

from .password_validation import validators
from .models import Usuario
from .utils.validacao_cpf import cpf
from .utils.validacao_email import email
from .utils.validacao_uf import uf
from apps.hidricos.models import Hidricos
from apps.clientes.models import Cliente


class RegisterResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'nome']


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, max_length=68, min_length=8, write_only=True)
    nome = serializers.CharField(max_length=100, required=False)
    cpf = serializers.CharField(required=True, max_length=11)
    estado = serializers.CharField(required=False, max_length=2)
    cidade = serializers.CharField(required=False)
    bacia_responsavel = serializers.CharField(required=True)
    cliente = serializers.CharField(required=True)

    class Meta:
        model = Usuario
        fields = ['id', 'email', 'password', 'nome', 'perfis', "cpf", "estado", "cidade", "bacia_responsavel", "cliente"]

    def validate_email(self, value):
        if not email(value):
            raise serializers.ValidationError("Email inválido.")
        
        try:
            user = Usuario.objects.get(email=value)
            if user:
                raise serializers.ValidationError("Usuário já cadastrado!")
        except Usuario.DoesNotExist:
            pass
        return value

    def validate_password(self, value):
        try:
            validate_password(value, password_validators=validators)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value
    
    def validate_cpf(self, value):
        if not cpf(value):
            raise serializers.ValidationError("CPF inválido.")
        return value
    
    def validate_estado(self, value):
        if not uf(value):
            raise serializers.ValidationError("Email inválido.")
        return value
    
    def validate_bacia_responsavel(self, value):
        try:
            bacia = Hidricos.objects.get(pk=value)
        except ValidationError as e:
            ...
        return bacia
    
    def validate_cliente(self, value):
        try:
            cliente = Cliente.objects.get(pk=value)
        except ValidationError as e:
            ...
        return cliente

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            nome=validated_data["nome"],
            cpf = validated_data["cpf"],
            estado = validated_data["estado"],
            cidade = validated_data["cidade"],
            bacia_responsavel = validated_data["bacia_responsavel"],
            cliente = validated_data["cliente"]
        )

        user.perfis.set(validated_data['perfis'])

        return user


class TokensSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()


class LoginRequestSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, max_length=68, min_length=8, write_only=True)

    class Meta:
        model = Usuario
        fields = ['email', 'password']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, max_length=68, min_length=8, write_only=True)

    tokens = serializers.SerializerMethodField(method_name='get_tokens')
    perfis = serializers.SerializerMethodField(method_name="get_perfis")

    class Meta:
        model = Usuario
        fields = ['email', 'password', 'tokens', 'perfis']

    @swagger_serializer_method(serializer_or_field=TokensSerializer)
    def get_tokens(self, obj):
        return TokensSerializer(obj['user'].tokens()).data
    
    def get_perfis(self, obj):
        return obj['perfis'].values_list('descricao', flat=True),

    def validate(self, attrs):
        print(attrs)
        email = attrs['email']
        password = attrs['password']

        user = authenticate(email=email, password=password)
        print(user)

        if not user:
            raise AuthenticationFailed('Invalid credentials.')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled.')
        
        return {
            'user': user,
            'perfis': user.perfis.all(),
            'email': user.email,
            'tokens': user.tokens,
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(LogoutSerializer, self).__init__(*args, **kwargs)
        self.token = None

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('Token is expired or invalid.')


class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ['email']

    def validate(self, attrs):
        email = attrs['email']

        try:
            worker = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("Funcionário não cadastrado!")

        return attrs


class ResetPasswordRequestSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, max_length=68, min_length=8, write_only=True)


class ResetPasswordConfirmSerializer(serializers.ModelSerializer):
    uidb64 = serializers.CharField(min_length=1, required=True, allow_blank=False)
    token = serializers.CharField(min_length=1, required=True, allow_blank=False)
    password = serializers.CharField(required=True, max_length=68, min_length=8, write_only=True)

    class Meta:
        model = Usuario
        fields = ['uidb64', 'token', 'password']

    def validate_password(self, value):
        try:
            validate_password(value, password_validators=validators)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value

    def validate(self, attrs):
        uidb64 = attrs['uidb64']
        token = attrs['token']

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = Usuario.objects.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            Usuario.DoesNotExist,
        ) as e:
            raise serializers.ValidationError(str(e))
        else:
            if not default_token_generator.check_token(user, token):
                raise serializers.ValidationError('Link está inválido.')

        attrs['user'] = user
        return attrs
