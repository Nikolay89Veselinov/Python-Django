from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class BasedViewsConfig(AppConfig):
    name = 'contrib.based_views'
    verbose_name = _('Based Views')
