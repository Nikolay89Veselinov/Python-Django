from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class OsmConfig(AppConfig):
    name = 'contrib.osm'
    verbose_name = _('Open Street Map')
