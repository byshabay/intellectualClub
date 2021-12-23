from django.core import exceptions
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *

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
        return Event.objects.filter(is_published=True)

# ABOUT US PAGE


def about(request):
    context = {
        'menu': menu,
        'title': 'О нас'
    }
    return render(request, 'main/about.html', context=context)


# EXCURTION PAGE

def excurtion(request):
    events = Event.objects.all()
    context = {
        'events': events,
        'menu': menu,
        'title': 'Экскурсии'
    }
    return render(request, 'main/category.html', context=context)


# SEMINARS PAGE

def seminars(request):
    events = Event.objects.all()
    context = {
        'events': events,
        'menu': menu,
        'title': 'Мастер классы'
    }
    return render(request, 'main/category.html', context=context)


# CHAT PAGE
def chat(request):
    return render(request, 'main/chat.html', {'title': 'Беседка'})


# SHOW EVENT CART

class ShowEventCart(DataMixin, DetailView):
    model = Event
    template_name = 'main/event.html'
    slug_url_kwarg = 'event_slug'
    context_object_name = 'event'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['event'])
        return dict(list(context.items()) + list(c_def.items()))

# CATEGORY


class EventCategory(DataMixin, ListView):
    model = Event
    template_name = 'main/index.html'
    context_object_name = 'events'
    allow_empty = False

    def get_queryset(self):
        return Event.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Категория - ' + str(context['events'][0].cat),
            cat_selected=context['events'][0].cat_id)
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
