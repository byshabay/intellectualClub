from django.conf import settings
from django.db import router

from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()


router.register('api/event', views.Test)
urlpatterns = [
    path('', views.EventHome.as_view(),  name="home"),
    path('about', views.about, name="about"),
    path('events/<slug:event_slug>', views.ShowEventCart.as_view(), name='event'),
    path('category/<slug:cat_slug>',
         views.EventCategory.as_view(), name="category"),
    path('addevents', views.AddEvent.as_view(), name='addevent'),

    path('event', views.test),


]

urlpatterns += router.urls
