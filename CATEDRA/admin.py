from django.contrib import admin
from .models import Escuela, Personal, Matricula, Destreza, Presupuesto, Visita, Actividad

# Register your models here.

admin.site.register(Escuela)
admin.site.register(Personal)
admin.site.register(Matricula)
admin.site.register(Destreza)
admin.site.register(Presupuesto)
admin.site.register(Visita)
admin.site.register(Actividad)
