from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,  name="home"),
    path('about', views.about, name="about"),
    path('category/excurtion', views.excurtion, name="excurtion"),
    path('category/seminars', views.seminars, name="seminars"),
    path('chat', views.chat, name="chat"),
    # path('category', views.excurtion, name="category")
]
