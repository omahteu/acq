from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=False)
    cnpj = models.CharField(max_length=18, null=True, blank=False, unique=True)
    telefone = models.CharField(max_length=11, null=True, blank=False)
    
    def __str__(self) -> str:
        return self.nome
