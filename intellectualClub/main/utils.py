# MAIN MENU

from django.db.models.aggregates import Count
from .models import *


menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Добавить событие', 'url_name': 'addevent'},
    {'title': 'Блог', 'url_name': 'posts'}
]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('event'))

        user_menu = menu.copy()

        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        context['menu'] = user_menu
        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context
