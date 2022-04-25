from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# POST MODEL START


class Post(models.Model):
    title = models.CharField('Название', max_length=255)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор')
    body = models.TextField('Содержимое')
    post_date = models.DateField('Дата добавления', auto_now_add=True)
    category = models.CharField(max_length=255, default='test')

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

# POST MOSEL END

# POST`S CATEGORIES START


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse('posts')

# POST`S CATEGORIES END
