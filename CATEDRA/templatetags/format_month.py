from django.template.defaultfilters import register

@register.filter(name='format_month')

def format_month(value):
    lista_meses = ['Meses', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Noviembre', 'Diciembre']

    return lista_meses[value]
