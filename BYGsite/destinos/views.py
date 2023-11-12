from django.http import HttpResponse,HttpResponseRedirect
from .temp_data import destino_data
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from .models import Destino
from django.views import generic


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
        destino_data.append({
            'name': request.POST['name'],
            'categoria': request.POST['categoria'],
            'descricao': request.POST['descricao'],
            'destino_url': request.POST['destino_url']
        })
        return HttpResponseRedirect(
            reverse('destinos:detail', args=(len(destino_data), )))
    else:
        return render(request, 'destinos/create.html', {})

def create_destino(request):
    if request.method == 'POST':
        destino_name = request.POST['name']
        destino_categoria = request.POST['categoria']
        destino_url = request.POST['destino_url']
        destino_descricao = request.POST['descricao']
        destino = Destino(name=destino_name,
                      categoria=destino_categoria,
                      destino_url=destino_url,
                      descricao=destino_descricao)
        destino.save()
        return HttpResponseRedirect(reverse('destinos:detail',
                                            args=(destino.id, )))
    else:
        return render(request, 'destinos/create.html', {})