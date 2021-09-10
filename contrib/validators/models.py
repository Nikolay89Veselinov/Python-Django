from django.db import models
from django.utils.translation import ugettext_lazy as _
from template_project.utils.validators import validate_even, phone_validator


class ValidatorModel(models.Model):
    even_field = models.IntegerField(validators=[validate_even], blank=True, null=True)
    phone = models.CharField('Телефон',
                                max_length=10,
                                validators=[phone_validator])
    name = models.CharField(_('First and last name'), max_length=254)
    description = models.TextField(_('Descriptions'))
    egn = models.CharField(_('EGN'), max_length=10)
    email = models.EmailField(_('E-mail'), blank=True)
    active = models.BooleanField(default=True)
    url = models.URLField()
    password = models.CharField(_('Password'), max_length=254)
    confirm_password = models.CharField(_('Confirm_password'), max_length=254)