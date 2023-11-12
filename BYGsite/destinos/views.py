from django.http import HttpResponse,HttpResponseRedirect
from .temp_data import destino_data
from django.shortcuts import render
from django.urls import reverse

def detail_destino(request, destino_id):
    context = {'destino': destino_data[destino_id - 1]}
    return render(request, 'destinos/detail.html', context)

def list_destinos(request):
    context = {"destino_list": destino_data}
    return render(request, 'destinos/index.html', context)

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
