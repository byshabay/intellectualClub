from django.urls import path
from . import views

urlpatterns = [
    path('order_created', views.order_created, name='order_created'),
    path('order/<int:pk>', views.order_creating, name='creating_oreder')
]
