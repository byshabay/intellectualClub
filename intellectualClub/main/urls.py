from django.conf import settings
from django.db import router

from django.urls import path, re_path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()


router.register('api/event', views.EventViewSet)
# router.register('^api/event/(?P<category>.+)/$',  views.EventViewSet)
urlpatterns = [
    path('', views.EventHome.as_view(),  name="home"),
    path('about', views.about, name="about"),
    path('events/<slug:event_slug>', views.ShowEventCart.as_view(), name='event'),
    path('category/<slug:cat_slug>',
         views.EventCategory.as_view(), name="category"),
    path('addevents', views.AddEvent.as_view(), name='addevent'),

    # path('event', views.test),
    # re_path('^api/event/(?P<category>.+)/$',  views.EventViewSet.as_view(),)


]

urlpatterns += router.urls
