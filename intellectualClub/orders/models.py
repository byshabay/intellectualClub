from django.db import models
from main.models import Event

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

# ORDERS TABLE START


class Order(models.Model):
    total_price = models.DecimalField(
        max_digits=10, decimal_places=0, default=0)  # total price for all events in order
    customer_email = models.EmailField(
        blank=True, null=True, default=None)
    customer_name = models.CharField(
        max_length=64, blank=True, null=True, default=None)
    customer_phone = models.CharField(
        max_length=48, blank=True, null=True, default=None)
    status = models.ForeignKey(Status,  on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

# ORDERS TABLE END

# EVENT IN ORDER TABLE START


class EventInOrder(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT, blank=True, null=True, default=None)
    event = models.ForeignKey(
        Event, on_delete=models.PROTECT, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(
        max_digits=10, decimal_places=0, default=0)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=0, default=0)  # price*nmb

    def __str__(self):
        return "%s" % self.event.title

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

    def save(self, *args, **kwargs):
        price_per_item = self.event.price
        self.price_per_item = price_per_item
        self.total_price = self.nmb * price_per_item

        super(EventInOrder, self).save(*args, **kwargs)

# EVENT IN ORDER TABLE END

# POST SAVE SIGNAL START


def event_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_events_in_order = EventInOrder.objects.filter(
        order=order, is_active=True)

    order_total_price = 0
    for item in all_events_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(event_in_order_post_save, sender=EventInOrder)

# POST SAVE SIGNAL END
