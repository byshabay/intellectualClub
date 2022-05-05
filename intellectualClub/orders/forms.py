from dataclasses import field
from django import forms
from orders.models import *


class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = EventOrder
        fields = ['total_price', 'customer_email',
                  'customer_name', 'customer_phone', 'event', 'date']

        widgets = {
            'total_price': forms.TextInput(attrs={'class': 'form-control', 'id': 'total_price', 'type': 'hidden'}),
            'customer_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш email', 'id': 'customer_email'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя', 'id': 'customer_name'}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш номер телефона'}),
            'event': forms.TextInput(attrs={'class': 'form-control', 'id': 'event_id', 'type': 'hidden'}),
            'date': forms.Select(attrs={'class': 'form-select'})
        }


class PreEventOreder(forms.ModelForm):
    class Meta:
        model = EventSchedule
        fields = '__all__'
