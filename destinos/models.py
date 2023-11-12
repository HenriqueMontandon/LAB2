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
    

class Roteiro(models.Model):
    author = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    destinos = models.ManyToManyField(Destino)

    def __str__(self):
        return f'{self.name} by {self.author}'
    
class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    movie = models.ForeignKey(Roteiro, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'