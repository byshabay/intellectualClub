from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from intellectualClub.settings import DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, mixins
from orders.forms import *
from orders.models import *
from rest_framework.generics import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import CreateEventOrderSerializer, ConsultationOrderSerializer

# Create your views here.

# 1.API EVENT ORDER CREATE START


class EventOrderAPIView(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = EventOrder.objects.all()
    serializer_class = CreateEventOrderSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# 1.API EVENT ORDER CREATE END

# 2.API CONSULTATION ORDER START


class ConsultationOrderMixin(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = ConsultationOrder.objects.all()
    serializer_class = ConsultationOrderSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# 2.API CONSULTATION ORDER END


# # CREATED OREDER


# def order_created(request):
#     return render(request, 'orders/created_order.html', {})

# # CREATING ORDER


# def order_creating(request, pk):
#     event = Event.objects.get(id=pk)
#     if request.method == 'GET':
#         form = OrderCreationForm()
#     elif request.method == 'POST':
#         form = OrderCreationForm(request.POST)
#         if form.is_valid():
#             subject = "Новый заказ на событие form.cleaned_data['event']"
#             from_email = form.cleaned_data['customer_email']
#             message = "Вам поступил новый заказ"
#             try:
#                 send_mail(f'{subject} от {from_email}', message,
#                           DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
#             except BadHeaderError:
#                 return HttpResponse('Ошибка в теме письма.')
#             form.save()
#             return redirect('order_created')
#     else:
#         return HttpResponse('Неверный запрос.')
#     return render(request, 'orders/creating_order.html', {'form': form, 'event': event})

    # form = OrderCreationForm
    # event = Event.objects.get(id=pk)

    # if request.method == 'POST':
    #     form = OrderCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('order_created')

    # return render(request, 'orders/creating_order.html', {'form': form, 'event': event})
