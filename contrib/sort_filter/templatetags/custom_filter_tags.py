from django import template

from contrib.sort_filter.models import Pub

register = template.Library()


@register.filter
def custom_lower(value):
    return value.lower()

@register.filter
def replace_text(b):
    s = ''
    for x in b:
        if x == 'a':
            s += ' work '
        else:
            s += x
    return s

@register.filter(is_safe=True)
def add_xx(value):
    return '%s work custom filter' % value

# return html
@register.simple_tag()
def simple_tag(context, text='Default'):
    return '<h1> simple_tg {} simple_tag {}</h1>'.format(context, text)


@register.inclusion_tag("template_tags/include_templatetags.html")
def inclusion_tag(country, text='inclusion_tags'):
    
    return {
        "country": country,
        'text': text,
        'pubs_count': Pub.objects.count()
    }

@register.inclusion_tag("template_tags/bootstrap.html")
def bootstrap_tag(form, action, method):

    for(_, field) in form.fields.items():
        if 'class' not in field.widget.attrs:
            field.widget.attrs['class'] = ''
        field.widget.attrs['class'] += 'form-control'

    
    return {
        "form": form,
        'action': action,
        'method': method,
    }