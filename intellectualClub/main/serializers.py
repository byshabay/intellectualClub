from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Event


class ShowEventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'price', 'discount',
                  'slug', 'description', 'short_description', 'photo', 'is_published', 'cat']
