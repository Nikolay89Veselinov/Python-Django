from django.contrib import admin

from .models import Country, City, Pub

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


@admin.register(Pub)
class PubAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'active', 'get_city', 'get_country')

    def get_city(self, obj):
            return obj.city

    def get_country(self, obj):
            return obj.city.country.name

    get_city.short_description = 'get city'
    get_country.short_description = 'get country'


    