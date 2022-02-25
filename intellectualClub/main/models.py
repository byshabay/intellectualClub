from distutils.command.clean import clean
from statistics import mode
from tabnanny import verbose
from django.db import models
from django.urls import reverse


# 1.EVENT TABLE START

class Event(models.Model):
    title = models.CharField('Название', max_length=50)
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    description = models.TextField('Описание')
    photo = models.ImageField(
        'Фото', upload_to="photos/%Y/%m/%d/", null=True)
    time_create = models.DateTimeField('Дата создания', auto_now_add=True)
    time_upload = models.DateTimeField('Дата изменения', auto_now=True)
    is_published = models.BooleanField('Публикация', default=True)
    cat = models.ForeignKey('Category',
                            on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

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
    date = models.DateTimeField('Дата и время проведения')
    status = models.BooleanField('Доступная дата / нет', default=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Расписание событий"
        verbose_name_plural = "Расписание событий"


# 3.EVENT SCHEDULE TABLE END
