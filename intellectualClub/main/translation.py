from dataclasses import fields
from modeltranslation.translator import register, TranslationOptions
from .models import Event, Category


@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description')


@register(Category)
class CategoryTranslationOprions(TranslationOptions):
    fields = ('name',)
