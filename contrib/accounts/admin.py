from django.contrib import admin
from .models import UsersProfile


@admin.register(UsersProfile)
class UsersProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
