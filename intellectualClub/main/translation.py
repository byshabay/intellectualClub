from dataclasses import fields
from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description')
