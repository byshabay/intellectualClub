
from django import views
from django.urls import path

from . import views


urlpatterns = [
    path('posts', views.PostsView.as_view(), name='posts'),
    path('article/<int:pk>', views.ArticleView.as_view(), name='article_detail'),
    path('add_post', views.AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', views.EditPostView.as_view(), name='edit_article'),

]
