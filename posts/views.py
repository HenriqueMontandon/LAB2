from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404, get_list_or_404,redirect
from django.urls import reverse, reverse_lazy
from .models import Post, Categorie, Comment
from django.views import generic, View
from django.views.generic import UpdateView, CreateView, DeleteView
from .forms import PostForm, CategorieForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

class DetailPost(generic.DetailView):
    model  = Post
    template_name = 'posts/detail.html'

class DeletePost(DeleteView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        if self.request.user == post.author or request.user.is_staff:
            post.delete()
            messages.success(request, 'Post deleted successfully.')
            return redirect('posts:index')  
        else:
            messages.error(request, 'You are not authorized to delete this post.')
            return redirect('posts:detail', pk=post.id)
        


class EditPost(UpdateView):
    model = Post
    fields = ['titulo', 'content', 'imagemCapa']
    template_name = 'posts/update.html'

    def form_valid(self, form):
        post = form.save(commit=False)

        # Check if the user is the author or an admin
        if self.request.user == post.author or self.request.user.is_staff:
            # User is authorized to edit the post
            messages.success(self.request, 'Post edited successfully.')
            return super().form_valid(form)
        else:
            # User is not authorized, show an error message or redirect as needed
            messages.error(self.request, 'You are not authorized to edit this post.')
            return redirect('posts:detail', pk=post.id)  # Redirect to post detail or any other desired URL

    def get_success_url(self):
        return reverse_lazy('posts:index')
    

class listPosts(generic.ListView):
    model = Post
    template_name = 'posts/index.html'

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('posts:detail', kwargs={'pk': self.object.id})
    


class CreateCategorieView(UserPassesTestMixin, View):
    template_name = 'posts/createCategorie.html'  
    form_class = CategorieForm  

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'You are not authorized to create a category.')
        return redirect('posts:index')  

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:listCategories')  

        return render(request, self.template_name, {'form': form})
    

class deleteCategorieView(LoginRequiredMixin, generic.DeleteView):
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        messages.error(self.request, 'You are not authorized to create a category.')
        return redirect('posts:index')
    
    model = Categorie
    template_name = 'posts/deleteCategorie.html'
    success_url = '/'

class listCategories(generic.ListView):
    model = Categorie
    template_name = 'posts/listCategories.html'

