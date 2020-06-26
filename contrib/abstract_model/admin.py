from django.contrib import admin
from .models import ChildA, ChildB


@admin.register(ChildA)
class ChildAAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name', 'last_name')


@admin.register(ChildB)
class ChildBAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name', 'last_name')
