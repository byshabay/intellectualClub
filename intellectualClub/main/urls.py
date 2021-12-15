from django.conf import settings

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,  name="home"),
    path('about', views.about, name="about"),
    path('category/excurtion', views.excurtion, name="excurtion"),
    path('category/seminars', views.seminars, name="seminars"),
    path('chat', views.chat, name="chat"),
    path('regiter', views.chat, name='register'),
    path('login', views.chat, name='login'),
    path('post/<int:post_id>', views.show_post, name='post'),
    path('category/<int:cat_id>', views.show_category, name="category")
]

