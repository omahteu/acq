from django.db import models
from apps.hidricos.models import Hidricos
from django.utils import timezone


class Microbiologico(models.Model):
    coliformes_totais = models.FloatField()
    coliformes_fecais = models.FloatField()
    e_coli = models.FloatField()
    bacia = models.ForeignKey(Hidricos, on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)
