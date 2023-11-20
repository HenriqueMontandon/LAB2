from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404, get_list_or_404
from django.urls import reverse, reverse_lazy
from .models import Destino, List
from django.views import generic
from .forms import DestinoForm, ReviewRoteiroForm, RoteiroForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.mixins import LoginRequiredMixin


def detail_destino(request, destino_id):
    destino = get_object_or_404(Destino, pk=destino_id)
    context = {"destino": destino}
    return render(request, "destinos/detail.html", context)


class DestinoListView(generic.ListView):
    model = Destino
    template_name = 'destinos/index.html'

def search_destinos(request):
    context = {}
    if request.GET.get("query", False):
        search_term = request.GET["query"].lower()
        destino_list = Destino.objects.filter(name__icontains=search_term)
        context = {"destino_list": destino_list}
    return render(request, "destinos/search.html", context)


@login_required
@permission_required('destinos.add_destino')
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
                          destino_url=destino_url,
                          likes=0)
            destino.save()
            return HttpResponseRedirect(
                reverse('destinos:detail', args=(destino.id, )))
    else:
        form = DestinoForm()
    context = {'form': form}
    return render(request, 'destinos/create.html', context)

class ListListView(generic.ListView):
    model = List
    template_name = 'destinos/lists.html'


class ListCreateView(LoginRequiredMixin, generic.CreateView):
    model = List
    template_name = 'destinos/create_roteiro.html'
    fields = ['Nome', 'atracoes', 'Capa']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('destinos:lists')

@login_required
def create_review(request, roteiro_id):
    roteiro = get_object_or_404(Destino, pk=roteiro_id)
    if request.method == 'POST':
        form = ReviewRoteiroForm(request.POST)
        if form.is_valid():
            review_author = request.user 
            review_text = form.cleaned_data['text']
            roteiro.review_set.create(author=review_author, text=review_text)
            return HttpResponseRedirect(
                reverse('destinos:roteiro',args=(roteiro_id,)))
    else:
        form = ReviewRoteiroForm()
        context = {'form': form, 'roteiro': roteiro}
    return render(request, 'destinos/review.html',context)

def RoteiroDetailView(request, pk):
     # Obtém a lista específica
    lista = List.objects.get(pk=pk)

    # Obtém os destino_id associados a essa lista
    destino_ids = List.objects.filter(pk=pk).values_list('atracoes', flat=True)

    # Obtém os destinos associados a esses destino_ids
    destinos = Destino.objects.filter(pk__in=destino_ids)

    return render(request, 'destinos/roteiro.html', {'destino_list': destinos})

class update_Roteiro(LoginRequiredMixin, generic.UpdateView):
    model = List
    template_name = 'destinos/update.html'
    fields = ['Nome', 'Destinos', 'Capa']
    success_url = reverse_lazy('destinos:lists')


class delete_Roteiro(LoginRequiredMixin, generic.DeleteView):
    model = List
    success_url = "/"
    template_name = "destinos/delete_roteiro.html"