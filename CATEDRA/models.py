from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from  datetime import datetime
from django.contrib.auth.models import User
from dal import autocomplete

# Create your models here.

class Municipio(models.Model):
    nombre_choices = (
    ('ADJUNTAS', 'ADJUNTAS'),
    ('AGUADA', 'AGUADA'),
    ('AGUADILLA', 'AGUADILLA'),
    ('AGUAS BUENAS', 'AGUAS BUENAS'),
    ('AGUAS BUENAS', 'AGUAS BUENAS'),
    ('ANASCO', 'ANASCO'),
    ('ARECIBO I', 'ARECIBO I'),
    ('ARECIBO II', 'ARECIBO II'),
    ('ARROYO', 'ARROYO'),
    ('BARCELONETA', 'BARCELONETA'),
    ('BARRANQUITAS', 'BARRANQUITAS'),
    ('BAYAMON I', 'BAYAMON I'),
    ('BAYAMON II', 'BAYAMON II'),
    ('BAYAMON III', 'BAYAMON III'),
    ('CABO ROJO', 'CABO ROJO'),
    ('CAGUAS I', 'CAGUAS I'),
    ('CAGUAS II', 'CAGUAS II'),
    ('CAMUY', 'CAMUY'),
    ('CANOVANAS', 'CANOVANAS'),
    ('CAROLINA I', 'CAROLINA I'),
    ('CAROLINA II', 'CAROLINA II'),
    ('CATANO', 'CATANO'),
    ('CAYEY', 'CAYEY'),
    ('CEIBA', 'CEIBA'),
    ('CIALES', 'CIALES'),
    ('CIDRA', 'CIDRA'),
    ('COAMO', 'COAMO'),
    ('COMERIO', 'COMERIO'),
    ('COROZAL', 'COROZAL'),
    ('CULEBRA', 'CULEBRA'),
    ('DORADO', 'DORADO'),
    ('FAJARDO', 'FAJARDO'),
    ('FLORIDA', 'FLORIDA'),
    ('GUANICA', 'GUANICA'),
    ('GUAYAMA', 'GUAYAMA'),
    ('GUAYANILLA', 'GUAYANILLA'),
    ('GUAYNABO', 'GUAYNABO'),
    ('GURABO', 'GURABO'),
    ('HATILLO', 'HATILLO'),
    ('HORMIGUEROS', 'HORMIGUEROS'),
    ('HUMACAO', 'HUMACAO'),
    ('ISABELA', 'ISABELA'),
    ('JAYUYA', 'JAYUYA'),
    ('JUANA DIAZ', 'JUANA DIAZ'),
    ('JUNCOS', 'JUNCOS'),
    ('LAJAS', 'LAJAS'),
    ('LARES', 'LARES'),
    ('LAS MARIAS', 'LAS MARIAS'),
    ('LAS PIEDRAS', 'LAS PIEDRAS'),
    ('LOIZA', 'LOIZA'),
    ('LUQUILLO', 'LUQUILLO'),
    ('MANATI', 'MANATI'),
    ('MARICAO', 'MARICAO'),
    ('MAUNABO', 'MAUNABO'),
    ('MAYAGUEZ', 'MAYAGUEZ'),
    ('MOCA', 'MOCA'),
    ('MOROVIS', 'MOROVIS'),
    ('NAGUABO', 'NAGUABO'),
    ('NARANJITO', 'NARANJITO'),
    ('OROCOVIS', 'OROCOVIS'),
    ('PATILLAS', 'PATILLAS'),
    ('PEÑUELAS', 'PEÑUELAS'),
    ('PONCE I', 'PONCE I'),
    ('PONCE II', 'PONCE II'),
    ('PONCE III', 'PONCE III'),
    ('QUEBRADILLAS', 'QUEBRADILLAS'),
    ('RINCON', 'RINCON'),
    ('RIO GRANDE', 'RIO GRANDE'),
    ('SABANA GRANDE', 'SABANA GRANDE'),
    ('SALINAS', 'SALINAS'),
    ('SAN GERMAN', 'SAN GERMAN'),
    ('SAN JUAN I', 'SAN JUAN I'),
    ('SAN JUAN II', 'SAN JUAN II'),
    ('SAN JUAN III', 'SAN JUAN III'),
    ('SAN JUAN IV', 'SAN JUAN IV'),
    ('SAN JUAN V', 'SAN JUAN V'),
    ('SAN LORENZO', 'SAN LORENZO'),
    ('SAN SEBASTIAN', 'SAN SEBASTIAN'),
    ('SANTA ISABEL', 'SANTA ISABEL'),
    ('TOA ALTA', 'TOA ALTA'),
    ('TOA BAJA', 'TOA BAJA'),
    ('TRUJILLO ALTO', 'TRUJILLO ALTO'),
    ('UTUADO', 'UTUADO'),
    ('VEGA ALTA', 'VEGA ALTA'),
    ('VEGA BAJA', 'VEGA BAJA'),
    ('VIEQUES', 'VIEQUES'),
    ('VILLALBA', 'VILLALBA'),
    ('YABUCOA', 'YABUCOA'),
    ('YAUCO', 'YAUCO'),
    )

    nombre = models.CharField(max_length=200, choices=nombre_choices)

    def __str__(self):
        return self.nombre


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
        ('Todos los niveles', 'Todos los niveles'),
    )

    tipo_choices = (
        ('Regular', 'Regular'),
        ('Educacion Especial', 'Educacion Especial'),
        ('Pre-vocaiconal', 'Pre-vocacional'),
        ('Especializada', 'Especializada'),
        ('Vocacional', 'Vocacional'),
    )

    zona_choices = (
        ('URBANA', 'URBANA'),
        ('RURAL', 'RURAL'),
    )

    operacional_choices = (
        ('SI', 'SI'),
        ('NO', 'NO'),
    )

    # Datos de usuario que genera el registro
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    # Datos generales de la escuela
    codigo = models.IntegerField(default=0, primary_key=True)
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(validators=[phone_regex], max_length=200, default='(000) 000-0000')
    fax = models.CharField(validators=[phone_regex], max_length=200, default='(000) 000-0000')
    region_educativa = models.CharField(max_length=200)
    distrito_escolar = models.CharField(max_length=200)
    municipio_escolar = models.CharField(max_length=200, null=True, blank=True)
    direccion_fisica = models.CharField(max_length=200, null=True, blank=True)
    direccion_zipcode = models.CharField(max_length=200, null=True, blank=True)
    #geolocalizacion = models.PointField(null=True, blank=True)
    zona = models.CharField(max_length=200, choices=zona_choices, default='RURAL')
    operacional = models.CharField(max_length=200, choices=operacional_choices, default='SI')
    nivel = models.CharField(max_length=200, choices=nivel_choices, default='Elemental')
    grados = models.CharField(max_length=200, null=True, blank=True)
    tipo = models.CharField(max_length=200, choices=tipo_choices, default='Regular')
    email = models.EmailField(max_length=254, null=True, blank=True)

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
    nombre_del_director = models.CharField(max_length=200, blank=True, null=True)
    estado_del_director = models.CharField(max_length=200, choices=estado_director_choices, blank=True, null=True)
    email_del_director = models.EmailField(max_length=254, null=True, blank=True)
    telefono_del_director = models.CharField(validators=[phone_regex], max_length=200, default='(000) 000-0000', blank=True, null=True)
    nombre_del_consejero = models.CharField(max_length=200, blank=True, null=True)
    email_del_consejero = models.EmailField(max_length=254, blank=True, null=True)
    telefono_del_consejero = models.CharField(validators=[phone_regex], max_length=200, default='(000) 000-0000', blank=True, null=True)
    nombre_del_trabajador_social = models.CharField(max_length=200, blank=True, null=True)
    email_del_trabajador_social = models.EmailField(max_length=254, blank=True, null=True)
    telefono_del_trabajador_social = models.CharField(validators=[phone_regex], max_length=200, default='(000) 000-0000', blank=True, null=True)
    nombre_del_requisante = models.CharField(max_length=200, blank=True, null=True)
    email_del_requisante = models.EmailField(max_length=254, blank=True, null=True)
    telefono_del_requisante = models.CharField(validators=[phone_regex], max_length=200, default='(000) 000-0000', blank=True, null=True)
    nombre_del_presidente_del_consejo_escolar = models.CharField(max_length=200, blank=True, null=True)
    telefono_del_presidente_del_consejo_escolar = models.CharField(validators=[phone_regex], max_length=200, default='(000) 000-0000', blank=True, null=True)


    # Datos de creacion y modificacion del registro
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        return "Personal Administrativo de " + self.escuela.nombre

class Matricula(models.Model):
    #Foreign Key de escuela
    escuela = models.OneToOneField(Escuela, primary_key=True, on_delete=models.CASCADE)

    #Datos generales de la matricula de la escuela
    matricula_de_estudiantes = models.IntegerField(default=0, blank=True, null=True)
    grado_infant = models.IntegerField(default=0, blank=True, null=True)
    grado_toddler = models.IntegerField(default=0, blank=True, null=True)
    grado_pk = models.IntegerField(default=0, blank=True, null=True)
    grado_pke = models.IntegerField(default=0, blank=True, null=True)
    grado_pkm = models.IntegerField(default=0, blank=True, null=True)
    grado_k = models.IntegerField(default=0, blank=True, null=True)
    grado_1 = models.IntegerField(default=0, blank=True, null=True)
    grado_2 = models.IntegerField(default=0, blank=True, null=True)
    grado_3 = models.IntegerField(default=0, blank=True, null=True)
    grado_4 = models.IntegerField(default=0, blank=True, null=True)
    grado_5 = models.IntegerField(default=0, blank=True, null=True)
    grado_6 = models.IntegerField(default=0, blank=True, null=True)
    grado_SGE = models.IntegerField(default=0, blank=True, null=True)
    grado_7 = models.IntegerField(default=0, blank=True, null=True)
    grado_8 = models.IntegerField(default=0, blank=True, null=True)
    grado_9 = models.IntegerField(default=0, blank=True, null=True)
    grado_SGI = models.IntegerField(default=0, blank=True, null=True)
    grado_10 = models.IntegerField(default=0, blank=True, null=True)
    grado_11 = models.IntegerField(default=0, blank=True, null=True)
    grado_12 = models.IntegerField(default=0, blank=True, null=True)
    grado_SGS = models.IntegerField(default=0, blank=True, null=True)
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
    espanol = models.CharField(max_length=200, blank=True, null=True)
    espanol_prebasico = models.FloatField(default=0, blank=True, null=True)
    espanol_basico = models.FloatField(default=0, blank=True, null=True)
    espanol_proficiente = models.FloatField(default=0, blank=True, null=True)
    espanol_avanzado = models.FloatField(default=0, blank=True, null=True)

    matematicas = models.CharField(max_length=200, blank=True, null=True)
    matematicas_prebasico = models.FloatField(default=0, blank=True, null=True)
    matematicas_basico = models.FloatField(default=0, blank=True, null=True)
    matematicas_proficiente = models.FloatField(default=0, blank=True, null=True)
    matematicas_avanzado = models.FloatField(default=0, blank=True, null=True)

    ingles = models.CharField(max_length=200, blank=True, null=True)
    ingles_prebasico = models.FloatField(default=0, blank=True, null=True)
    ingles_basico = models.FloatField(default=0, blank=True, null=True)
    ingles_proficiente = models.FloatField(default=0, blank=True, null=True)
    ingles_avanzado = models.FloatField(default=0, blank=True, null=True)

    prioridad = models.CharField(max_length=200, blank=True, null=True)
    materia_prioridad = models.CharField(max_length=200, blank=True, null=True)

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

    class Meta:
        get_latest_by = "fecha"

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

class Empleado(models.Model):
    rol_choices = (
    ('Administrativo', 'Administrativo'),
    ('Vendedor', 'Vendedor'),
    )

    phone_regex = RegexValidator(
                    regex='^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$',
                    message="El telefono debe ser suministrado con el siguiente formato: '(787) 549-1004'."
                    )


    def upload_to(instance, filename):
        return 'imagenes/%s/%s' % (instance.usuario.username, filename)

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=200, choices=rol_choices, default='Vendedor')
    avatar = models.ImageField(upload_to=upload_to, null=True, blank=True)
    municipio = models.ManyToManyField(Municipio, blank=True)
    telefono = models.CharField(validators=[phone_regex], max_length=200, default='(000) 000-0000')

    def __str__(self):
        return self.usuario.first_name + self.usuario.last_name

class Propuesta(models.Model):
    estado_choices = (
    ('CREADA', 'CREADA'),
    ('EN EVALUACION', 'EN EVALUACION'),
    ('RECHAZADA', 'RECHAZADA'),
    ('NO INTERES', 'NO INTERES'),
    ('P.O. GENERADO', 'P.O. GENERADO'),
    )

    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    estado = models.CharField(max_length=200, choices=estado_choices, default='CREADA')

class CodigosDE(models.Model):
    codigo = models.IntegerField(primary_key=True)
    modalidad = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    costo = models.IntegerField(default=0)

    def __str__(self):
        return str(self.codigo) + " " + self.modalidad



class Ofrecimiento(models.Model):
    estado_choices = (
    ('EN EVALUACION', 'EN EVALUACION'),
    ('APROBADA', 'APROBADA'),
    ('RECHAZADA', 'RECHAZADA'),
    )

    estado = models.CharField(max_length=200, choices=estado_choices, default='EN EVALUACION')
    propuesta = models.ForeignKey(Propuesta, on_delete=models.CASCADE, null=True, blank=True)
    codigode = models.ForeignKey(CodigosDE, on_delete=models.CASCADE)
    materia = models.CharField(max_length=200)
    estrategia = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    horas = models.IntegerField(default=0)
    participantes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.codigode.codigo) + " - " + self.codigode.modalidad + " / " + self.titulo

class PurchaseOrder(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    propuesta = models.ForeignKey(Propuesta, on_delete=models.CASCADE)
    ofrecimiento = models.ManyToManyField(Ofrecimiento)
    numero = models.CharField(max_length=200)
    documento = models.FileField(upload_to='registros/po/')
