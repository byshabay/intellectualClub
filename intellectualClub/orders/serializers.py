
from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import EventOrder, ConsultationOrder

# 1.EVENT ORDER SERIALIZER START


class CreateEventOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventOrder
        fields = ['total_price', 'customer_email',
                  'customer_name', 'customer_phone', 'event']

# 1. EVENT ORDER SERIALIZER END

# 2.CONSULTATION ORDER START


class ConsultationOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationOrder
        fields = ['customer_email', 'customer_phone',
                  'customer_name', 'language', 'comment']

# 2.CONSULTATION ORDER END
