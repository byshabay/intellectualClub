from django.contrib import admin
from theblog.models import Category, Post
from modeltranslation.admin import TranslationAdmin

# Register your models here.


class PostAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'header_image', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'body')
    list_filter = ('post_date', )


admin.site.register(Post, PostAdmin)


# class CategoryAdmin(TranslationAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id', 'name')
#     search_fields = ('name',)


admin.site.register(Category)
