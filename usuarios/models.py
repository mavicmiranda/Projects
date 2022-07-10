from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
