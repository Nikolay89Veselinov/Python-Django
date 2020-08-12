from django.db import models
from django.utils.html import format_html


class AdminTricks(models.Model):

    MONTH_CHOICES = (
        ('JANUARY', "January"),
        ('FEBRUARY', "February"),
        ('MARCH', "March"),
        ('APRIL', "April"),
        ('MAY', "May"),
        ('JUNE', "June"),
        ('JULY', "July"),
        ('AUGUST', "August"),
        ('SEPTEMBER', "September"),
        ('OCTOBER', "October"),
        ('NOVEMBER', "November"),
        ('DECEMBER', "December"),
    )

    first_name = models.CharField('Име', max_length=50, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=50, blank=True, null=True)
    eng = models.CharField('ЕГН', max_length=10, blank=True, null=True)
    phone = models.CharField('Мобилен телефон', max_length=10, blank=True, null=True)
    email = models.EmailField('E-mail',max_length=150, blank=True, null=True)
    birthday = models.DateTimeField()
    color_code = models.CharField(max_length=6, blank=True, null=True)
    month = models.CharField(max_length=9, choices=MONTH_CHOICES, default='JANUARY')
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.first_name
    
    def colored_name(self):
        return format_html(
            '<span style="color: #{};">{} {}</span>',
            self.color_code,
            self.first_name,
            self.last_name,
        )

    def decade_born_in(self):
        return self.birthday.strftime('%Y / %A / week number of the year %W / day of the year %j') + " / some string"
    decade_born_in.short_description = 'Birth decade'