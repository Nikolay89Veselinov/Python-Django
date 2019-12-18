from django.contrib import admin
from .forms import OpenStreetMapsForm

from .models import OpenStreetMaps


@admin.register(OpenStreetMaps)
class OpenStreetMapsAdmin(admin.ModelAdmin):
    list_display = ('location', 'location_lat', 'location_lon')
    form = OpenStreetMapsForm
