from django.contrib import admin

from .models import ASD

@admin.register(ASD)
class ASDAdmin(admin.ModelAdmin):
    pass