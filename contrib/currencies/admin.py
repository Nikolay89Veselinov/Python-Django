from django.contrib import admin
from .models import Currency

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['currency', 'course', 'date']
    list_filter = ('date', )

admin.site.register(Currency, CurrencyAdmin)


