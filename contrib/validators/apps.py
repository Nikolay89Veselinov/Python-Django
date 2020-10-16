from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class ValidatorsConfig(AppConfig):
    name = 'contrib.validators'
    verbose_name = _('Validators')