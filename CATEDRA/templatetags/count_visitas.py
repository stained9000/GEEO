from django.template.defaultfilters import register
from datetime import datetime

@register.filter(name='count_visitas')

def count_visitas(escuela):
    mes = datetime.now().month

    return len(escuela.visita_set.filter(fecha__month=mes)) 
