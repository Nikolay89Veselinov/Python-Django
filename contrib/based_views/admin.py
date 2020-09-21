from django.contrib import admin

from .models import Article


@admin.register(Article)
class Article(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'active', )
