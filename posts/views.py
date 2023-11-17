from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404, get_list_or_404,redirect
from django.urls import reverse, reverse_lazy
from .models import Post, Categorie, Comment
from django.views import generic, View
from django.views.generic import UpdateView, CreateView 
from .forms import PostForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class DetailPost(generic.DetailView):
    model  = Post
    template_name = 'posts/detail.html'


class DeletePost(View):
    @login_required
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)

        # Check if the user is the author or an admin
        if request.user == post.author or request.user.is_staff:
            # User is authorized to delete the post
            post.delete()
            messages.success(request, 'Post deleted successfully.')
            return redirect('posts:index')  # Redirect to the post list or any other desired URL
        else:
            # User is not authorized, show an error message or redirect as needed
            messages.error(request, 'You are not authorized to delete this post.')
            return redirect('posts:detail', post_id=post.id)
        


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
            return redirect('posts:detail', post_id=post.id)  # Redirect to post detail or any other desired URL

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
        return reverse_lazy('posts:detail', kwargs={'post_id': self.object.id})
