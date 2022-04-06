from dataclasses import field
from pyexpat import model
from re import template
from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from theblog.models import Post
from theblog.forms import PostForm

# Create your views here.

# LIST OF POSTS


class PostsView(ListView):
    model = Post
    template_name = 'theblog/posts.html'

# SIMPLE ARTICLE


class ArticleView(DetailView):
    model = Post
    template_name = 'theblog/article_details.html'


# ADD POST

class AddPostView(CreateView):
    model = Post
    form_class = PostForm

    template_name = 'theblog/add_post.html'

# EDIT POST


class EditPostView(UpdateView):
    model = Post
    form_class = PostForm

    template_name = 'theblog/edit_article.html'
