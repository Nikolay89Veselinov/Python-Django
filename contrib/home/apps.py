from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class HomeConfig(AppConfig):
    name = 'contrib.home'
    verbose_name = _('Home')
