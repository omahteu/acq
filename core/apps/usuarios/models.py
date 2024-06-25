from django.contrib.auth.models import Group, Permission, BaseUserManager, PermissionsMixin, AbstractBaseUser
from ..clientes.models import Cliente
from django.db import models


class Perfil(models.Model):
    perfil_id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=300)
    status = models.BooleanField(null=False)
    
    def __str__(self) -> str:
        return self.descricao
