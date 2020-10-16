from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AbstractModelConfig(AppConfig):
    name = 'contrib.abstract_model'
    verbose_name = _('Abstract model')
