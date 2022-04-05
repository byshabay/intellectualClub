import profile
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(
        "Изображение", null=True, upload_to='photos/profile_pic/')

    def __str__(self):
        return "%s" % self.user

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
