
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


phone_validator = RegexValidator(regex=r'^[0-9]{10,254}$',
                                 message=('Въведения мобилен телефон'
                                          'е невалиден'))


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )

