from django_filters import rest_framework as filters
from main.models import Event


class EventCategoryFilter(filters.FilterSet):

    class Meta:
        model = Event
        fields = ['cat', 'cat__is_active',
                  'is_published', 'is_promo', 'is_popular']
