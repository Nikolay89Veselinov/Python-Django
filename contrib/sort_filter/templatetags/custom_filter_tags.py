from django import template

register = template.Library()


@register.filter
def custom_lower(value):
    return value.lower()

@register.filter(is_safe=True)
def add_xx(value):
    return '%s work custom filter' % value