from re import template
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .forms import *
from .models import *

# MAIN MENU

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Регистрация', 'url_name': 'login'},
    {'title': 'Вход', 'url_name': 'login'},
    {'title': 'Добавить событие', 'url_name': 'addevent'}
]


# HOME PAGE

class EventHome(ListView):
    model = Event
    template_name = 'main/index.html'
    context_object_name = 'events'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

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

class ShowEventCart(DetailView):
    model = Event
    template_name = 'main/event.html'
    slug_url_kwarg = 'event_slug'
    context_object_name = 'event'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['event']
        return context

# CATEGORY


class EventCategory(ListView):
    model = Event
    template_name = 'main/index.html'
    context_object_name = 'events'
    allow_empty = False

    def get_queryset(self):
        return Event.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория - ' + str(context['events'][0].cat)
        context['cat_selected'] = context['events'][0].cat_id
        return context

# ADD NEW EVENTS


# def addevent(request):

#     if(request.method == 'POST'):
#         form = AddEventForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddEventForm()

#     return render(request, 'main/addevent.html', {'form': form, 'menu': menu, 'title': 'Добавить событие'})

class AddEvent(CreateView):
    form_class = AddEventForm
    template_name = 'main/addevent.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление события'
        return context
