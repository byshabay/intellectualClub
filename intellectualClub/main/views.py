from django.shortcuts import render
from .models import Event

# HOME PAGE


def index(request):
    events = Event.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'events': events})


# ABOYT US PAGE

def about(request):
    return render(request, 'main/about.html')


# EXCURTION PAGE

def excurtion(request):
    events = Event.objects.all()
    return render(request, 'main/category.html', {'title': 'Экскурсии', 'events': events, 'type': 'экскурсия'})


# SEMINARS PAGE

def seminars(request):
    events = Event.objects.all()
    return render(request, 'main/category.html', {'title': 'Мастер классы', 'events': events, 'type': 'мастер-класс'})


# CHAT PAGE
def chat(request):
    return render(request, 'main/chat.html')
