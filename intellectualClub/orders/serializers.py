
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import EventOrder


class CreateEventOrderSerializer(ModelSerializer):
    class Meta:
        model = EventOrder
        fields = ['total_price', 'customer_email',
                  'customer_name', 'customer_phone', 'event', 'date']
