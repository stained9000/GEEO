from django.template.defaultfilters import register

@register.filter(name='po_total')

def po_total(ofrecimiento_list):
    total = 0

    for ofrecimiento in ofrecimiento_list:
        if ofrecimiento.codigode.codigo == 11829:
            total += ofrecimiento.codigode.costo * ofrecimiento.participantes
        else:
            total += ofrecimiento.codigode.costo
    return total
