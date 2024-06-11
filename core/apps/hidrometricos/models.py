from django.db import models


class Hidrometrico(models.Model):
    pressao = models.FloatField()
    nivel_agua = models.FloatField()
    vazao = models.FloatField()
    consumo = models.FloatField()
    
    def __str__(self) -> str:
        return super().__str__()
