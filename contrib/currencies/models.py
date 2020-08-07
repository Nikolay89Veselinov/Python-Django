from django.db import models


class Currency(models.Model):
    currency = models.CharField(max_length=255, blank=False, null=False)
    course = models.DecimalField(max_digits=32, decimal_places=5)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.currency
