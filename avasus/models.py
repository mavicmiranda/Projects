from django.db import models
from datetime import datetime

class Avasus(models.Model):
    nome_curso = models.CharField(max_length=200)
    descricao = models.TextField()
    objetivo = models.TextField(null=True)
    idade = models.IntegerField()
    ch = models.IntegerField(null=True)
    data_curso = models.DateTimeField(default=datetime.now, blank=True)
    modulos = models.IntegerField(null=True)