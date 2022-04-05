
from django import views
from django.urls import path

from . import views


urlpatterns = [
    path('posts', views.PostsView.as_view(), name='posts'),
    path('article/<int:pk>', views.ArticleView.as_view(), name='article_detail')
]
