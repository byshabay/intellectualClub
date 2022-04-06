from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
