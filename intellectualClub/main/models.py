from django.db import models
from django.urls import reverse


# 1.EVENT TABLE START

class Event(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    photo = models.ImageField(
        'Фото', upload_to="photos/%Y/%m/%d/", null=True)
    time_create = models.DateTimeField('Дата создания', auto_now_add=True)
    time_upload = models.DateTimeField('Дата изменения', auto_now=True)
    is_published = models.BooleanField('Публикация', default=True)
    cat = models.ForeignKey('Category',
                            on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"
        ordering = ['-time_create', 'title']

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

# 1.EVENT TABLE END

# 2.EVENT CATEGORY TABLE START


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name='Название категории')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'

        # 2.EVENT CATEGORY TABLE END
