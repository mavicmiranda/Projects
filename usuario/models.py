from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    CPF = models.IntegerField()
    email = models.CharField(max_length=200)