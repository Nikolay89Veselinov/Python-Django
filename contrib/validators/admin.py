from django.contrib import admin

from .models import ValidatorModel


@admin.register(ValidatorModel)
class ValidatorModelAdmin(admin.ModelAdmin):
    pass
