from django.template.defaultfilters import register

@register.filter(name='format_mayus')

def format_mayus(value):
    return value.upper()
