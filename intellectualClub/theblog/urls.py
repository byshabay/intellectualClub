from django import views
from django.urls import path

from . import views


urlpatterns = [
    path('posts', views.PostsView.as_view(), name='posts'),
    path('article/<int:pk>', views.ArticleView.as_view(), name='article_detail'),
    path('add_post', views.AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', views.EditPostView.as_view(), name='edit_article'),
    path('article/<int:pk>/delete',
         views.DeletePostView.as_view(), name='delete_article'),
    path('posts/add_category', views.AddCategoryView.as_view(),
         name='add_post_category'),
    path('post_category/<str:cats>/',
         views.PostCategoryView, name='post_category'),
    path('like/<int:pk>', views.LikeView, name='like_post'),


]
