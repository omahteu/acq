from django.db import models


class FisicoQuimico(models.Model):
    alcalinidade_hidroxidos = models.FloatField()
    alcalinidade_bicarbonato = models.FloatField()
    alcalinidade_carbonato = models.FloatField()
    alcalinidade_total = models.FloatField()
    aluminio = models.FloatField()
    cloreto = models.FloatField()
    condutividade_eletrica_25 = models.FloatField()
    cor_verdadeira = models.FloatField()
    cor_aparente = models.FloatField()
    dureza_calcio = models.FloatField()
    dureza_magnesio = models.FloatField()
    dureza_total = models.FloatField()
    estimativa_tds = models.FloatField()
    ferro_total = models.FloatField()
    fluoreto = models.FloatField()
    manganes = models.FloatField()
    nitrato = models.FloatField()
    nitrito = models.FloatField()
    ph = models.FloatField()
    potassio = models.FloatField()
    silica = models.FloatField()
    sodio = models.FloatField()
    solidos_totais = models.FloatField()
    sulfatos = models.FloatField()
    turbidez = models.FloatField()
    oxigenio_dissolvido = models.FloatField()
    cloro_residual_livre = models.FloatField()
