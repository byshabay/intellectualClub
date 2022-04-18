from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from theblog.models import Post
from theblog.forms import PostForm

# Create your views here.

# LIST OF POSTS


class PostsView(ListView):
    model = Post
    template_name = 'theblog/posts.html'
    ordering = ['-post_date']

# SIMPLE ARTICLE


class ArticleView(DetailView):
    model = Post
    template_name = 'theblog/article_details.html'


# ADD POST

class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    raise_exception = True

    template_name = 'theblog/add_post.html'

# EDIT POST


class EditPostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    raise_exception = True

    template_name = 'theblog/edit_post.html'

# DELETE POST


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'theblog/delete_post.html'
    raise_exception = True
    success_url = reverse_lazy('home')
