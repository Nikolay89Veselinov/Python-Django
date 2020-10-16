from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class AdminTricksConfig(AppConfig):
    name = 'contrib.admin_tricks'
    verbose_name = _('Admin tricks app')
