from dataclasses import fields
from modeltranslation.translator import register, TranslationOptions
from theblog.models import Post, Category


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'snippet')


# @register(Category)
# class CategoryTranslationOprions(TranslationOptions):
#     fields = ('name',)
