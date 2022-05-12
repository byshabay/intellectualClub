import imp
from django_filters import rest_framework as filters
from main.models import Event


class EventCategoryFilter(filters.FilterSet):

    class Meta:
        model = Event
        fields = ['cat_id', ]
