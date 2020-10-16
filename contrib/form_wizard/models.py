from django.db import models
from django.utils.translation import ugettext_lazy as _


class Client(models.Model):
    first_name = models.CharField(_('Име'), max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    eng = models.CharField('ЕГН', max_length=10)
    phone = models.CharField('Мобилен телефон', max_length=10)
    email = models.EmailField('E-mail',max_length=150)


class WritingClient(models.Model):
    first_name = models.CharField(_('Име'), max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    eng = models.CharField('ЕГН', max_length=10)
    phone = models.CharField('Мобилен телефон', max_length=10)
    email = models.EmailField('E-mail',max_length=150)