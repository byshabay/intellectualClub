from re import T
from tkinter import N
from tkinter.messagebox import NO
from django.db import models
from django.urls import reverse


# 1.EVENT TABLE START

class Event(models.Model):
    title = models.CharField('Название', max_length=50)
    price = models.DecimalField(
        max_digits=10, decimal_places=0, default=0)
    discount = models.IntegerField(blank=True, null=True, default=0)
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    short_description = models.TextField(
        'Краткое описание', blank=True, null=True, default=None)
    description = models.TextField('Описание')
    photo = models.ImageField(
        'Фото', upload_to="photos/%Y/%m/%d/", null=True)
    time_create = models.DateTimeField('Дата создания', auto_now_add=True)
    time_upload = models.DateTimeField('Дата изменения', auto_now=True)
    is_published = models.BooleanField('Публикация', default=True)
    cat = models.ForeignKey('Category',
                            on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return "%s %s" % (self.price, self.title)

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"
        ordering = ['-time_create', 'title']

    def get_absolute_url(self):
        return reverse('event', kwargs={'event_slug': self.slug})

# 1.EVENT TABLE END

# 2.EVENT CATEGORY TABLE START


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name='Название категории')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'

# 2.EVENT CATEGORY TABLE END

# 3.EVENT SCHEDULE TABLE START


class EventSchedule(models.Model):
    event = models.ForeignKey(
        'Event', on_delete=models.PROTECT, verbose_name='Событие')
    date = models.DateTimeField('Дата и время проведения', unique=True)
    status = models.BooleanField('Доступная дата / нет', default=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Расписание событий"
        verbose_name_plural = "Расписание событий"


# 3.EVENT SCHEDULE TABLE END

# 4.EVENT IMAGE TABLE START

class EventImage(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, blank=True, null=True, default=None)
    photo = models.ImageField(
        'Фото', upload_to="photos/%Y/%m/%d/", null=True)
    is_active = models.BooleanField(default=True)
    time_create = models.DateTimeField('Дата создания', auto_now_add=True)
    time_upload = models.DateTimeField('Дата изменения', auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

# 4.EVENT IMAGE TABLE END
