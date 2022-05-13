from django.contrib import admin
from orders.models import *
from modeltranslation.admin import TranslationAdmin

# 1.STATUS START


class StatusAdmin(TranslationAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)

# 1.STATUS END


admin.site.register(EventOrder)

# 2. ORDER A CONSULTATION START


class ConsultationOrderAdmin(admin.ModelAdmin):
    list_display = ('id',  'customer_email',
                    'customer_phone', 'customer_name', 'status', 'language', 'comment')
    search_fields = ('created', 'customer_email',
                     'customer_phone', 'customer_name')
    list_editable = ('status',)
    list_display_links = ('id', 'customer_email', 'customer_phone')


admin.site.register(ConsultationOrder, ConsultationOrderAdmin)

# 2. ORDER A CONSULTATION END
