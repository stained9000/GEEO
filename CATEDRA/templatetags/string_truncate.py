from django.template.defaultfilters import register

@register.filter(name='string_truncate')

def string_truncate(string):
    if len(string) > 23:
        return string[0:23] + '...'
    else:
        return string
