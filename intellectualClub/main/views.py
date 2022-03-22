from cgi import test
from pyexpat import model
from re import template

from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core import exceptions
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from rest_framework.viewsets import ModelViewSet
from django.views.generic.base import TemplateView

from .forms import *
from .models import *
from .utils import *
from .serializers import ShowEventSerializer

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

class ShowEventCart(DataMixin, DetailView):
    model = Event
    template_name = 'main/event.html'
    slug_url_kwarg = 'event_slug'
    context_object_name = 'event'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title=context['event'], schedule=EventSchedule.objects.filter(event=context['event'], status='True'))

        return dict(list(context.items()) + list(c_def.items()))


class Test(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = ShowEventSerializer


def test(request):
    return render(request, 'main/test.html')


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

#  REGISTER USER CLASS


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация пользователей')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


# LOGIN USER CLASS

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwarg):
        context = super().get_context_data(**kwarg)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

# LOGOUT USER


def logout_user(request):
    logout(request)
    return redirect('login')


# USER ACCOUNT
class UserAccount(LoginRequiredMixin, DataMixin, TemplateView):
    model = User
    template_name = 'main/account.html'
    raise_exception = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Мой аккаунт')
        return dict(list(context.items()) + list(c_def.items()))
