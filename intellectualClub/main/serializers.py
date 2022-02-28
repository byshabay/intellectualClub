from dataclasses import field
from multiprocessing import Event
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import Event


class ShowEventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'description']
