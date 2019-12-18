from django.db import models

from osm_field.fields import LatitudeField, LongitudeField, OSMField


class OpenStreetMaps(models.Model):
    location = OSMField()
    location_lat = LatitudeField()
    location_lon = LongitudeField()
