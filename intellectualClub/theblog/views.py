
from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from theblog.models import *
from theblog.forms import PostForm
from django.http import HttpResponseRedirect

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

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context['total_likes'] = total_likes
        return context


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

# ADD CATEGORY


class AddCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'theblog/add_category.html'
    fields = '__all__'
    raise_exception = True
    success_url = reverse_lazy('posts')

# SHOW CATEGORY


def PostCategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'theblog/post_categories.html', {'cats': cats, 'category_posts': category_posts})


# LIKE POST

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))
