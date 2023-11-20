from django.forms import ModelForm
from .models import Post, Comment, Categorie

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'titulo',
            'content',
            'imagemCapa',
            'categoria'
        ]

class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        fields = [
            'name'
        ]