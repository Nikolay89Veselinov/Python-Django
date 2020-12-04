from django.contrib import admin
from .models import Pet, Like, Comment


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'age', 'description', 'image_url')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('pet',)


admin.site.register(Comment)