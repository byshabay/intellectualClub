from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Event


class ShowEventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'price', 'discount',
                  'slug', 'author', 'author_language', 'description', 'short_description', 'photo', 'date', 'is_published', 'is_popular', 'is_promo', 'cat', 'meta']
