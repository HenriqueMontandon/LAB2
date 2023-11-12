from django.forms import ModelForm
from .models import Destino, Review

class DestinoForm(ModelForm):
    class Meta:
        model = Destino
        fields = [
            'name',
            'categoria',
            'descricao',
            'destino_url',
        ]
class ReviewRoteiroForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'text',
        ]
        labels = {
            'text': 'Resenha',
        }