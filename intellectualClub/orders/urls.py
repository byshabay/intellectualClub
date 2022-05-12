from django.db import router
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()


urlpatterns = [
    path('order_created', views.order_created, name='order_created'),
    path('order/<int:pk>', views.order_creating, name='creating_oreder'),
    path('api/event_order/<int:pk>', views.EventOrderMixin.as_view()),

]

urlpatterns += router.urls
