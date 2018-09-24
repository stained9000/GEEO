from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Escuela, Personal, Matricula, Destreza, Presupuesto, Visita, Actividad, Empleado, Municipio, CodigosDE, Propuesta, Ofrecimiento, PurchaseOrder

# Register your models here.

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmpleadoInline(admin.StackedInline):
    model = Empleado
    can_delete = False
    verbose_name_plural = 'empleado'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmpleadoInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Escuela)
admin.site.register(Personal)
admin.site.register(Matricula)
admin.site.register(Destreza)
admin.site.register(Presupuesto)
admin.site.register(Visita)
admin.site.register(Actividad)
admin.site.register(Municipio)
admin.site.register(CodigosDE)
admin.site.register(Ofrecimiento)
admin.site.register(Propuesta)
admin.site.register(PurchaseOrder)
