from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class CrudOperationConfig(AppConfig):
    name = 'contrib.crud_operation'
    verbose_name = _('Crud Operations')
