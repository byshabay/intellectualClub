from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# POST MODEL START


class Post(models.Model):
    title = models.CharField('Название', max_length=255)
    header_image = models.ImageField(
        null=True, blank=True, upload_to="photos/%Y/%m/%d/")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор')

    body = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=255, default='Test')
    post_date = models.DateField('Дата добавления', auto_now_add=True)
    category = models.CharField(max_length=255, default='test')
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

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
