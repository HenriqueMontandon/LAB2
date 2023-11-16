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
    likes = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.likes}'
    

class List(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Nome = models.CharField(max_length=255)
    Capa = models.URLField(max_length=5000, null=True)
    Destinos = models.ManyToManyField(Destino)

    def __str__(self):
        return f'{self.Nome} by {self.autor.username}'
    
class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'