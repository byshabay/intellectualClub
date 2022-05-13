from django.contrib import admin
from .models import *

from modeltranslation.admin import TranslationAdmin


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 0


class CategoryMetaDataInline(admin.TabularInline):
    model = CategoryMetaData
    extra = 0


class EventScheduleInline(admin.TabularInline):
    model = EventSchedule
    extra = 0


class EventAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ("title",)}
    # inlines = [EventImageInline, EventScheduleInline]


class CategoryMetaDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'cat')


class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ("name",)}
    inlines = [CategoryMetaDataInline]


class EventScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'date', 'status')
    search_fields = ('date',)
    list_editable = ('status',)


class EventImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EventImage._meta.fields]

    class Meta:
        model = EventImage


admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(EventSchedule, EventScheduleAdmin)
admin.site.register(EventImage, EventImageAdmin)
admin.site.register(CategoryMetaData, CategoryMetaDataAdmin)
admin.site.register(GroupOfMetaData)
