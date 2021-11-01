from django.db import models


class Event(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    type = models.CharField('Тип', max_length=50, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"
