from django.db import models
from main.models import Event, EventSchedule

from django.db.models.signals import post_save

# Create your models here.

# STATUS TABLE START


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'

# STATUS TABLE END

# EVENT ORDERS TABLE START


class EventOrder(models.Model):
    total_price = models.DecimalField(
        max_digits=10, decimal_places=0, default=0)  # total price for all events in order
    customer_email = models.EmailField(
        blank=True, null=True, default=None)
    customer_name = models.CharField(
        max_length=64, blank=True, null=True, default=None)
    customer_phone = models.CharField(
        max_length=48, blank=True, null=True, default=None)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    status = models.ForeignKey(Status,  on_delete=models.PROTECT, default=1)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(EventOrder, self).save(*args, **kwargs)

# EVENT ORDERS TABLE END

# 7. ORDER A CONSULTATION START


class ConsultationOrder(models.Model):
    ENGLISH = 'EN'
    FRENCH = 'FR'
    RUSSIAN = 'RUS'
    # GERMAN = 'GER'
    LANGUAGES = [
        (ENGLISH, 'English'),
        (FRENCH, 'French'),
        (RUSSIAN, 'Russian'),
        # (GERMAN, 'German'),
    ]
    customer_email = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255)
    language = models.CharField(
        max_length=3,
        choices=LANGUAGES,
        default=ENGLISH,
    )
    comment = models.TextField()
    status = models.ForeignKey(Status,  on_delete=models.PROTECT, default=1)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ на консультацию №%s" % (self.id)

# 7. ORDER A CONSULTATION END
