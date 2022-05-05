from django.shortcuts import redirect, render
from orders.models import *
from orders.forms import *
from django.urls import reverse_lazy

# Create your views here.

# CREATED OREDER


def order_created(request):
    return render(request, 'orders/created_order.html', {})

# CREATING ORDER


def order_creating(request, pk):
    form = OrderCreationForm
    event = Event.objects.get(id=pk)

    if request.method == 'POST':
        form = OrderCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_created')

    return render(request, 'orders/creating_order.html', {'form': form, 'event': event})
