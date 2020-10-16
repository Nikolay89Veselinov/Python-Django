from django.db import models
from django.utils.translation import ugettext_lazy as _

class Currency(models.Model):
    currency = models.CharField(max_length=255, blank=False, null=False)
    course = models.DecimalField(max_digits=32, decimal_places=5)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')

    def __str__(self):
        return self.currency
