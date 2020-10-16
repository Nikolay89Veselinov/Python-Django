from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class SortFilterConfig(AppConfig):
    name = 'contrib.sort_filter'
    verbose_name = _('Sort and Filter')
