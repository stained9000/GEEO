from django.template.defaultfilters import register

@register.filter(name='multiply')

def multiply(costo, participantes):
    return costo * participantes
