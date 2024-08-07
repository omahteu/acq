from django.db import models
from apps.hidricos.models import Hidricos
from django.utils import timezone


class Hidrometrico(models.Model):
    pressao = models.FloatField()
    nivel_agua = models.FloatField()
    vazao = models.FloatField()
    # consumo = models.FloatField()
    bacia = models.ForeignKey(Hidricos, on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)
    
    def __str__(self) -> str:
        return super().__str__()
