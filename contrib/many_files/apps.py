from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class ManyFilesConfig(AppConfig):
    name = 'contrib.many_files'
    verbose_name = _('Many Files')
