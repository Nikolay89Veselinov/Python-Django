from django.contrib import admin

from .models import File, FileCollection, Form, Image


class FileAdmin(admin.StackedInline):
    list_display = ('files', )
    model = File
    extra = 2

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 3
        if obj and obj.parent:
            return max_num - 1
        return max_num

@admin.register(FileCollection)
class FileCollectionAdmin(admin.ModelAdmin):
    inlines = [FileAdmin]


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

