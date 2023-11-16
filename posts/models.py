from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=1000)
    criacaodata = models.DateTimeField(auto_now_add=True)
    ateracaodata = models.DateTimeField(auto_now= True)
    likes = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titulo} - {self.likes}'

class Categorie(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.name}'

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    criacaodata = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario feito por {self.author.username} em {self.criacaodata}'

