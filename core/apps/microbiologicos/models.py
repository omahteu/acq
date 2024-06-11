from django.db import models


class Microbiologico(models.Model):
    coliformes_totais = models.FloatField()
    coliformes_fecais = models.FloatField()
    e_coli = models.FloatField()
