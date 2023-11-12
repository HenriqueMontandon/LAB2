from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Destino, Roteiro
from django.views import generic
from .forms import DestinoForm


class DestinoDetailView(generic.DetailView):
    model = Destino
    template_name = 'destinos/detail.html'

class DestinoListView(generic.ListView):
    model = Destino
    template_name = 'destinos/index.html'

def search_destinos(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "destino_list": [
                m for m in destino_data
                if request.GET['query'].lower() in m['name'].lower()
            ]
        }
    return render(request, 'destinos/search.html', context) 

def create_destino(request):
    if request.method == 'POST':
        form = DestinoForm(request.POST)
        if form.is_valid():
            destino_name = form.cleaned_data['name']
            destino_categoria = form.cleaned_data['categoria']
            destino_descricao = form.cleaned_data['descricao']
            destino_url = form.cleaned_data['destino_url']
            destino = Destino(name=destino_name,
                          categoria=destino_categoria,
                          descricao=destino_descricao,
                          destino_url=destino_url)
            destino.save()
            return HttpResponseRedirect(
                reverse('destinos:detail', args=(destino.id, )))
    else:
        form = DestinoForm()
    context = {'form': form}
    return render(request, 'destinos/create.html', context)

class RoteiroListView(generic.ListView):
    model = Roteiro
    template_name = 'destinos/roteiros.html'

class ListCreateView(generic.CreateView):
    model = Roteiro
    template_name = 'destinos/create_roteiro.html'
    fields = ['name', 'author', 'destinos']
    success_url = reverse_lazy('destinos:lists')