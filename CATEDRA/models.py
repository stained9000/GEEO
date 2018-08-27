from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from  datetime import datetime


# Create your models here.

class Escuela(models.Model):
    phone_regex = RegexValidator(
                    regex='^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$',
                    message="El telefono debe ser suministrado con el siguiente formato: '(787) 549-1004'."
                    )

    nivel_choices = (
        ('Elemental', 'Elemental'),
        ('Superior', 'Superior'),
        ('Intermedio', 'Intermedio'),
        ('Segunda Unidad', 'Segunda Unidad'),
    )

    tipo_choices = (
        ('Regular', 'Regular'),
        ('Educacion Especial', 'Educacion Especial'),
        ('Pre-vocaiconal', 'Pre-vocacional'),
        ('Especializada', 'Especializada'),
        ('Vocacional', 'Vocacional'),
    )

    # Datos de usuario que genera el registro
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    # Datos generales de la escuela
    codigo = models.IntegerField(default=0, primary_key=True)
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(validators=[phone_regex], max_length=200, default='(000) 000-0000')
    fax = models.CharField(validators=[phone_regex], max_length=200, default='(000) 000-0000')
    region_educativa = models.CharField(max_length=200)
    distrito_escolar = models.CharField(max_length=200)
    nivel = models.CharField(max_length=200, choices=nivel_choices, default='Elemental')
    tipo = models.CharField(max_length=200, choices=tipo_choices, default='Regular')


    # Datos de creacion y modificacion del registro
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateField(auto_now=True)


    def __str__(self):
        return self.nombre


class Personal(models.Model):
    phone_regex = RegexValidator(
                    regex='^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$',
                    message="El telefono debe ser suministrado con el siguiente formato: '(787) 549-1004'."
                    )

    estado_director_choices = (
        ('En propiedad', 'En propiedad'),
        ('Interino', 'Interino'),
    )

    #Foreign Key de escuela
    escuela = models.OneToOneField(Escuela, primary_key=True, on_delete=models.CASCADE)

    #Datos generales del Personal Administrativo de la Escuela
    nombre_del_director = models.CharField(max_length=200)
    estado_del_director = models.CharField(max_length=200, choices=estado_director_choices, default='En propiedad')
    email_del_director = models.EmailField(max_length=254)
    telefono_del_director = models.CharField(validators=[phone_regex], max_length=200, default='(000) 000-0000')
    nombre_del_consejero = models.CharField(max_length=200)
    email_del_consejero = models.EmailField(max_length=254)
    telefono_del_consejero = models.CharField(validators=[phone_regex], max_length=200, default='(000) 000-0000')
    nombre_del_trabajador_social = models.CharField(max_length=200)
    email_del_trabajador_social = models.EmailField(max_length=254)
    telefono_del_trabajador_social = models.CharField(validators=[phone_regex], max_length=200, default='(000) 000-0000')
    nombre_del_requisante = models.CharField(max_length=200)
    email_del_requisante = models.EmailField(max_length=254)
    telefono_del_requisante = models.CharField(validators=[phone_regex], max_length=200, default='(000) 000-0000')
    nombre_del_presidente_del_consejo_escolar = models.CharField(max_length=200)
    telefono_del_presidente_del_consejo_escolar = models.CharField(validators=[phone_regex], max_length=200, default='(000) 000-0000')


    # Datos de creacion y modificacion del registro
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        return "Personal Administrativo de " + self.escuela.nombre

class Matricula(models.Model):
    #Foreign Key de escuela
    escuela = models.OneToOneField(Escuela, primary_key=True, on_delete=models.CASCADE)

    #Datos generales de la matricula de la escuela
    matricula_de_estudiantes = models.IntegerField(default=0)
    maestros_de_espanol = models.IntegerField(default=0)
    maestros_de_matematicas = models.IntegerField(default=0)
    maestros_de_ingles = models.IntegerField(default=0)
    maestros_de_ciencias = models.IntegerField(default=0)
    maestros_otros = models.IntegerField(default=0)


    # Datos de creacion y modificacion del registro
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        return "Matricula de " + self.escuela.nombre

"""
class Necesidad(models.Model):
    #Foreign Key de escuela
    escuela = models.OneToOneField(Escuela, primary_key=True, on_delete=models.CASCADE)

    #Datos generales de las necesidades de la Escuela

    #Nivel Elemental (K-6) Español
    comprension_auditiva_k6_e = models.BooleanField()
    expresion_oral_k6_e = models.BooleanField()
    destrezas_fundamentales_lectura_k6_e = models.BooleanField()
    dominio_de_la_lengua_k6_e = models.BooleanField()
    escritura_y_produccion_de_textos_k6_e = models.BooleanField()

    #Nivel Secundario (7-12) Español
    comprension_auditiva_712_e = models.BooleanField()
    expresion_oral_712_e = models.BooleanField()
    destrezas_fundamentales_lectura_712_e = models.BooleanField()
    dominio_de_la_lengua_712_e = models.BooleanField()
    escritura_y_produccion_de_textos_712_e = models.BooleanField()

    #Nivel Elemental (K-6) Matematica
    numeracion_operacion_k6_m = models.BooleanField()
    algebra_k6_m = models.BooleanField()
    analisis_de_datos_y_probabilidad_k6_m = models.BooleanField()

    #Nivel Secundario (7-12) Matematica
    medicion_712_m = models.BooleanField()
    geometria_712_m = models.BooleanField()
    funciones_712_m = models.BooleanField()

    #Misc
    listening = models.BooleanField()
    writing = models.BooleanField()
    reading = models.BooleanField()
    language = models.BooleanField()

    #Datos de creacion y modificacion del registro
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        return "Necesidades de " + self.escuela.nombre
"""

class Destreza(models.Model):
    #Foreign Key de la escuela
    escuela = models.OneToOneField(Escuela, primary_key=True, on_delete=models.CASCADE)

    #Datos de destrezas de la escuela
    espanol = models.CharField(max_length=200)
    matematicas = models.CharField(max_length=200)
    ingles = models.CharField(max_length=200)
    prioridad = models.CharField(max_length=200)
    materia_prioridad = models.CharField(max_length=200)

    #Datos de creacion y modificacion del registro
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        return "Destrezas de " + self.escuela.nombre

class Presupuesto(models.Model):
    presupuesto_choices = (
        ('1290', '1290'),
        ('1290 B', '1290 B'),
        ('Titulo II', 'Titulo II'),
    )

    #Foreign Key de escuela
    escuela = models.OneToOneField(Escuela, primary_key=True, on_delete=models.CASCADE)

    #Datos de presupuesto de la escuela
    presupuesto_asignado = models.CharField(max_length=200, choices=presupuesto_choices, null=True, blank=True)

    #Datos de creacion y modificacion del registro
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        return "Presupuesto de " + self.escuela.nombre

class Visita(models.Model):
    #Foreign Key de la Escuela
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)

    #Datos de Usuario
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    #Datos de la Visita
    fecha = models.DateField(default=timezone.now)
    anotaciones = models.CharField(max_length=200)
    hoja_de_visita = models.FileField(upload_to='registros/visitas/')

    #Datos modificacion del registro
    fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        return "Visita a la escuela " + self.escuela.nombre


class Actividad(models.Model):
    estado_choices = (
        ('Propuesta', 'Propuesta'),
        ('Aprobada', 'Aprobada'),
        ('Rechazada', 'Rechazada'),
        ('En proceso', 'En proceso'),
        ('Completado', 'Completado'),
    )

    tipo_choices = (
        ('CATEDRA-Maestros', 'CATEDRA-Maestros'),
        ('HELP-Padres', 'HELP-Padres'),
    )

    #Foreign Key de la Escuela
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)

    #Datos de Usuario
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    #Datos de la actividad de la escuela
    estado = models.CharField(max_length=10, choices=estado_choices, default='En proceso')
    tipo = models.CharField(max_length=200, choices=tipo_choices)
    taller_sugerido = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=timezone.now)
    horario = models.CharField(max_length=200)

    #Datos de creacion y modificacion del registro
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Actividad de la escuela " + self.escuela.nombre
