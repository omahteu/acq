from django.db import models


class Hidricos(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=False)
    estado = models.CharField(max_length=50, null=True, blank=True)
    status = models.BooleanField(null=True)
    
    def __str__(self) -> str:
        return self.nome
