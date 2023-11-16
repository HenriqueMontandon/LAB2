from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404, get_list_or_404
from django.urls import reverse, reverse_lazy
from .models import Post, Categorie, Comment
from django.views import generic
from .forms import PostForm, CategorieForm, CommentForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.mixins import LoginRequiredMixin

