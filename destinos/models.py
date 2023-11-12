from django.db import models
from django.conf import settings

class Empresa(models.Model):
    CNPJ = models.CharField(max_length=255)
    nomeFantasia = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nomeFantasia}'

class Destino(models.Model):
    name = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    destino_url = models.URLField(max_length=200, null=True)
    descricao = models.CharField(max_length=1000)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    likes = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.likes}'