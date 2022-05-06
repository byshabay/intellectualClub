from django.shortcuts import redirect, render
from orders.models import *
from orders.forms import *
from django.urls import reverse_lazy
from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from intellectualClub.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
# Create your views here.

# CREATED OREDER


def order_created(request):
    return render(request, 'orders/created_order.html', {})

# CREATING ORDER


def order_creating(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == 'GET':
        form = OrderCreationForm()
    elif request.method == 'POST':
        form = OrderCreationForm(request.POST)
        if form.is_valid():
            subject = "Новый заказ на событие form.cleaned_data['event']"
            from_email = form.cleaned_data['customer_email']
            message = "Вам поступил новый заказ"
            try:
                send_mail(f'{subject} от {from_email}', message,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            form.save()
            return redirect('order_created')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, 'orders/creating_order.html', {'form': form, 'event': event})

    # form = OrderCreationForm
    # event = Event.objects.get(id=pk)

    # if request.method == 'POST':
    #     form = OrderCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('order_created')

    # return render(request, 'orders/creating_order.html', {'form': form, 'event': event})
