
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


from .forms import *
from .models import *
from .serializers import ShowEventSerializer, ShowPromoEventSerializer
from .service import EventCategoryFilter
from .utils import *


# Event List

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = ShowEventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventCategoryFilter

# Popular Event


class PromoEventViewSet(ReadOnlyModelViewSet):
    queryset = Event.objects.filter(is_promo=True)
    serializer_class = ShowPromoEventSerializer
