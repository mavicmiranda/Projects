from django.db import models
from cpf_field.models import CPFField

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    CPF = CPFField('CPF', max_length=14)
    email = models.CharField(max_length=200)