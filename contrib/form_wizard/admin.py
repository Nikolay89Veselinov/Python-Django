from django.contrib import admin

from .models import Client, WritingClient

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'eng', 'phone', 'email')


@admin.register(WritingClient)
class WritingClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'eng', 'phone', 'email')
