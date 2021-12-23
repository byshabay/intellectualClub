from django.conf import settings

from django.urls import path

from . import views

urlpatterns = [
    path('', views.EventHome.as_view(),  name="home"),
    path('about', views.about, name="about"),
    path('regiter', views.chat, name='register'),
    path('login', views.chat, name='login'),
    path('events/<slug:event_slug>', views.ShowEventCart.as_view(), name='event'),
    path('category/<slug:cat_slug>',
         views.EventCategory.as_view(), name="category"),
    path('addevents', views.AddEvent.as_view(), name='addevent')

]
