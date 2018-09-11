from django import forms

from .models import Escuela, Personal, Matricula, Actividad, Destreza, Presupuesto, Visita, Propuesta, Ofrecimiento

class EscuelaForm(forms.ModelForm):

    class Meta:
        model = Escuela
        fields = ('codigo', 'nombre', 'telefono', 'fax', 'region_educativa', 'distrito_escolar', 'nivel',  'tipo')

class PersonalForm(forms.ModelForm):

    class Meta:
        model = Personal
        fields = ('nombre_del_director', 'estado_del_director', 'email_del_director', 'telefono_del_director', 'nombre_del_consejero', 'email_del_consejero', 'telefono_del_consejero', 'nombre_del_trabajador_social', 'email_del_trabajador_social', 'telefono_del_trabajador_social', 'nombre_del_requisante', 'email_del_requisante', 'telefono_del_requisante', 'nombre_del_presidente_del_consejo_escolar', 'telefono_del_presidente_del_consejo_escolar')

class MatriculaForm(forms.ModelForm):

    class Meta:
        model = Matricula
        fields = ('matricula_de_estudiantes', 'maestros_de_espanol', 'maestros_de_matematicas', 'maestros_de_ingles', 'maestros_de_ciencias', 'maestros_otros')

class DestrezaForm(forms.ModelForm):

    class Meta:
        model = Destreza
        fields = ('espanol', 'matematicas', 'ingles', 'prioridad', 'materia_prioridad')

class PresupuestoForm(forms.ModelForm):

    class Meta:
        model = Presupuesto
        fields = ('presupuesto_asignado',)


class VisitaForm(forms.ModelForm):

    class Meta:
        model = Visita
        fields = ('escuela', 'anotaciones', 'hoja_de_visita',)

class ActividadForm(forms.ModelForm):

    class Meta:
        model = Actividad
        fields = ('estado', 'tipo', 'taller_sugerido', 'fecha', 'horario',)

class PropuestaForm(forms.ModelForm):

    class Meta:
        model = Propuesta
        fields = ('escuela', 'fecha', 'estado',)

class OfrecimientoForm(forms.ModelForm):

    class Meta:
        model = Ofrecimiento
        fields = ('codigode', 'materia', 'estrategia', 'titulo', 'horas', 'participantes' )
