# MAIN MENU

from django.db.models.aggregates import Count
from .models import *


menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Регистрация', 'url_name': 'login'},
    {'title': 'Вход', 'url_name': 'login'},
    {'title': 'Добавить событие', 'url_name': 'addevent'}
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('event'))

        user_menu = menu.copy()

        if not self.request.user.is_authenticated:
            user_menu.pop(4)

        context['menu'] = user_menu
        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context
