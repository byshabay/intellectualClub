from modeltranslation.translator import register, TranslationOptions
from .models import Status


@register(Status)
class StatusTranslationOptions(TranslationOptions):
    fields = ('name', )
