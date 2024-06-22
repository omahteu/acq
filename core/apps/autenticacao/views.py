from drf_yasg.utils import swagger_auto_schema

from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from .models import Usuario
from .serializers import (
    RegisterSerializer,
    RegisterResponseSerializer,
    LoginSerializer,
    LoginRequestSerializer,
    LogoutSerializer,
    ResetPasswordSerializer,
    ResetPasswordRequestSerializer,
    ResetPasswordConfirmSerializer
)
from .utils.task import send_email
from .utils.helper import check_request_data


class RegisterView(GenericAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=RegisterSerializer, responses={status.HTTP_200_OK: RegisterResponseSerializer})
    def post(self, request):
        data = request.data
        if check_request_data(data, ["email", "password", "nome", "perfis", "cpf", "bacia_responsavel", "cliente"]):
            return Response(
                {'error': 'Content is not corrected.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=LoginRequestSerializer, responses={status.HTTP_200_OK: LoginSerializer})
    def post(self, request):
        data = request.data
        
        if check_request_data(data, ['email', 'password']):
            return Response(
                {'error': 'Content is not corrected.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        login_serializer = self.serializer_class(data=data)
        login_serializer.is_valid(raise_exception=True)

        user = login_serializer.validated_data['user']
        login(request, user)

        return Response(login_serializer.data, status=status.HTTP_200_OK)


class LogoutView(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            logout(request)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TokenError:
            return Response(
                {'error': 'Token is expired or invalid.'},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ResetPasswordView(GenericAPIView):
    queryset = Usuario.objects.all()
    serializer_class = ResetPasswordSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(responses={status.HTTP_200_OK: ''}, security=[])
    def post(self, request):
        data = request.data
        if check_request_data(data, ['email']):
            return Response(
                {'error': 'Content is not corrected.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.queryset.get(email=serializer.data['email'])
        data_email = {
            'domain': settings.FRONTEND_URL
            if settings.FRONTEND_URL
            else get_current_site(request).domain,
            'user': user.email,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
            'subject': 'Alteração de senha.',
        }
        send_email.delay(data_email, 'authentication/reset_password.html')
        return Response(status=status.HTTP_200_OK)


class ResetPasswordConfirmView(GenericAPIView):
    serializer_class = ResetPasswordConfirmSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        request_body=ResetPasswordRequestSerializer,
        responses={status.HTTP_200_OK: ""},
        security=[],
    )
    def post(self, request, uidb64=None, token=None):
        serializer = self.serializer_class(
            data={"uidb64": uidb64, "token": token, **request.data}
        )
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response(status=status.HTTP_200_OK)
