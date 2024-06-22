from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

from ..usuarios.models import Perfil
from ..clientes.models import Cliente
from ..hidricos.models import Hidricos

from django.contrib.auth.models import Group, Permission


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.staff = True
        user.active = True
        user.is_superuser = True
        user.perfis.add(Perfil.objects.get(descricao="Gestor"))
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    perfis = models.ManyToManyField(Perfil)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    bacia_responsavel = models.ForeignKey(Hidricos, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    staff = models.BooleanField(
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )
    active = models.BooleanField(
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')

    class Meta:
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {'refresh': str(refresh), 'access': str(refresh.access_token)}

    @property
    def is_staff(self) -> bool:
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_active(self) -> bool:
        "Is the user active?"
        return self.active

    @property
    def is_admin(self) -> bool:
        "Is the user an admin member?"
        return self.is_superuser
