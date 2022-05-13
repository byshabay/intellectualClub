
from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer
from .models import EventOrder


class CreateEventOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventOrder
        fields = ['total_price', 'customer_email',
                  'customer_name', 'customer_phone', 'event', 'date']

        # def create(self, validated_data):
        #     # pass all parameters from serializer
        #     request = Request.start_request(**validated_data)
        #     return request
