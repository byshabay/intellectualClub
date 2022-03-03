from django.contrib import admin
from orders.models import *

# 1.INLINES START


class EventInOrderInline(admin.TabularInline):
    model = EventInOrder
    extra = 0

# 1.INLINES END

# 2.STATUS START


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)

# 2.STATUS END

# 3.ORDER START


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [EventInOrderInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)

# 3.ORDER END

# 4.EVENT IN ORDER START


class EventInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EventInOrder._meta.fields]

    class Meta:
        model = EventInOrder


admin.site.register(EventInOrder, EventInOrderAdmin)

# 4.EVENT IN ORDER END
