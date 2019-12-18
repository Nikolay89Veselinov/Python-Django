from django.contrib import admin

from .models import File, FileCollection, Form


class FileAdmin(admin.StackedInline):
    list_display = ('files', )
    model = File
    extra = 1


@admin.register(FileCollection)
class FileCollectionAdmin(admin.ModelAdmin):
    inlines = [FileAdmin]


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('name', )