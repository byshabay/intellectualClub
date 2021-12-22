from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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


def index(request):
    events = Event.objects.all()
    context = {
        'events': events,
        'menu': menu,
        'title': 'Главная страница сайта',
        'cat_selected': 0
    }
    return render(request, 'main/index.html', context=context)


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


# SHOW PRODUCT CART

def show_post(request, post_slug):
    post = get_object_or_404(Event, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'main/post.html', context=context)

# CATEGORY


def show_category(request, cat_slug):
    cats = Category.objects.get(slug=cat_slug)
    events = Event.objects.filter(cat_id=cats.pk)

    if len(events) == 0:
        raise Http404()

    context = {
        'events': events,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cats.pk,
    }
    return render(request, 'main/index.html', context=context)


# ADD NEW EVENTS
def addevent(request):

    if(request.method == 'POST'):
        form = AddEventForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddEventForm()

    return render(request, 'main/addevent.html', {'form': form, 'menu': menu, 'title': 'Добавить событие'})
