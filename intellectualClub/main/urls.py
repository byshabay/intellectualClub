from django.conf import settings

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,  name="home"),
    path('about', views.about, name="about"),
    path('regiter', views.chat, name='register'),
    path('login', views.chat, name='login'),
    path('post/<slug:post_slug>', views.show_post, name='post'),
    path('category/<slug:cat_slug>', views.show_category, name="category"),
    path('addevents', views.addevent, name='addevent')

]
