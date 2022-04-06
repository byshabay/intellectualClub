from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView

from theblog.models import Post

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
    template_name = 'theblog/add_post.html'
    fields = '__all__'
