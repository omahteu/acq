from django.db import models
from ..hidricos.models import Hidricos


class Localidade(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    endereco = models.CharField(max_length=300, null=False, blank=False)
    latitude = models.CharField(max_length=300, null=False, blank=False)
    longitude = models.CharField(max_length=300, null=False, blank=False)
    hidricos = models.ForeignKey(Hidricos, on_delete=models.PROTECT, null=True)
    
    def __str__(self) -> str:
        return super().__str__()
