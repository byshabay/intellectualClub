from django.conf import settings
from django.db import router

from django.urls import path, re_path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()


router.register('api/event', views.EventViewSet)
router.register('api/promo_event', views.PromoEventViewSet)
urlpatterns = [

]

urlpatterns += router.urls
