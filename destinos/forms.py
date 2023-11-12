from django.forms import ModelForm
from .models import Destino, Review, List

class DestinoForm(ModelForm):
    class Meta:
        model = Destino
        fields = [
            'name',
            'categoria',
            'descricao',
            'destino_url',
        ]
class RoteiroForm(ModelForm):
    class Meta:
        model = List
        fields = [
            'Nome',
            'Capa',
            'autor',
            'Destinos'
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