from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import BadHeaderError, send_mail
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django_filters.rest_framework import DjangoFilterBackend
from intellectualClub.settings import EMAIL_HOST_USER
from orders.forms import PreEventOreder
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .forms import *
from .models import *
from .serializers import ShowEventSerializer
from .service import EventCategoryFilter
from .utils import *

from account.views import IsUser

# HOME PAGE


class EventHome(DataMixin, ListView):
    model = Event
    template_name = 'main/index.html'
    context_object_name = 'events'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Event.objects.filter(is_published=True).select_related('cat')

# ABOUT US PAGE


def about(request):
    context = {
        'menu': menu,
        'title': 'О нас'
    }
    return render(request, 'main/about.html', context=context)


# SHOW EVENT CART

class ShowEventCart(DataMixin, DetailView, FormView):
    model = Event
    form_class = PreEventOreder
    template_name = 'main/event.html'
    slug_url_kwarg = 'event_slug'
    context_object_name = 'event'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title=context['event'], schedule=EventSchedule.objects.filter(event=context['event'], status='True'))

        return dict(list(context.items()) + list(c_def.items()))

# Event List JSON


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = ShowEventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventCategoryFilter

    # @action(detail=True, methods=['post'])
    # def get_category(self, request, **kwargs):
    #     category = self.kwargs['cat']
    #     return Event.objects.filter(cat__id == category)

# CATEGORY


class EventCategory(DataMixin, ListView):
    model = Event
    template_name = 'main/index.html'
    context_object_name = 'events'
    allow_empty = False

    def get_queryset(self):
        return Event.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(
            title='Категория - ' + str(c.name),
            cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))

# ADD NEW EVENTS


class AddEvent(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddEventForm
    template_name = 'main/addevent.html'
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление события')
        return dict(list(context.items()) + list(c_def.items()))
