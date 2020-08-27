from django.db import models
from template_project.utils.validators import validate_even, phone_validator


class ValidatorModel(models.Model):
    even_field = models.IntegerField(validators=[validate_even])
    phone = models.CharField('Телефон',
                                max_length=10,
                                validators=[phone_validator])
