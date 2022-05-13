from django.db import router
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ConsultationOrderMixin, EventOrderAPIView

router = SimpleRouter()


urlpatterns = [
    # path('order_created', views.order_created, name='order_created'),
    # path('order/<int:pk>', views.order_creating, name='creating_oreder'),
    path('api/event_order/',
         EventOrderAPIView.as_view(), name='event_order'),
    path('api/consultation_order/', ConsultationOrderMixin.as_view())

]

urlpatterns += router.urls
