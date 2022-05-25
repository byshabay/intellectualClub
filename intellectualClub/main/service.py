from unicodedata import name
from django_filters import rest_framework as filters
from main.models import Event


class EventCategoryFilter(filters.FilterSet):
    price = filters.RangeFilter()

    class Meta:
        model = Event
        fields = ['price', 'cat', 'cat__is_active',
                  'is_published', 'is_promo', 'is_popular']
