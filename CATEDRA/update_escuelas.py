#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

# import pandas as pd
from sodapy import Socrata
from .models import Escuela, Personal, Matricula, Destreza
from django.utils import timezone

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.pr.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.pr.gov,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("ceib-pqg3", limit=2000)

# Convert to pandas DataFrame
# results_df = pd.DataFrame.from_records(result_list)

for escuela in results:
    #Creacion o update de escuelas
    escuela_obj, escuela_created = Escuela.objects.update_or_create(
            codigo = escuela['codigo'],
            defaults={
            'nombre': escuela['escuela'],
            'telefono': '(787) ' + escuela['telefono'],
            'fax' : '(787) ' + escuela['fax'],
            'region_educativa' : escuela['region'],
            'distrito_escolar' : escuela['distrito'],
            'municipio_escolar' : escuela['municipio_escolar'],
            'direccion_fisica' : escuela['direccion_fisica'],
            'direccion_zipcode' : escuela['direccion_zipcode'],
            'zona' : escuela['zona'],
            'operacional' : escuela['estatus_actual'],
            'nivel' : escuela['nivel_original'],
            'grados' : escuela['grados_posterior'],
            }
            )

    if escuela_created:
        escuela_obj.fecha_creacion = timezone.now
        escuela_obj.fecha_modificacion = timezone.now
        escuela_obj.save()
    else:
        escuela_obj.fecha_modificacion = timezone.now
        escuela_obj.save()


    #Creacion o update de personal de las Escuelas
    #La data solo contiene informacion del director. La otra debe ser llenada manual.

    personal_obj, personal_created = Personal.objects.update_or_create(
           escuela = escuela_obj,
           defaults={
           'nombre_del_director' : escuela['director'],
           }
           )

    if personal_created:
        personal_obj.fecha_creacion = timezone.now
        personal_obj.fecha_modificacion = timezone.now
        personal_obj.save()
    else:
        personal_obj.fecha_modificacion = timezone.now
        personal_obj.save()


    #Creacion o update de matricula de la escuela

    matricula_obj, matricula_created = Matricula.objects.update_or_create(
           escuela = escuela_obj,
           defaults={
           'matricula_de_estudiantes' : escuela['matricula_total'],
           'grado_infant' : escuela.get('grado_infant'),
           'grado_toddler' : escuela.get('grado_toddler'),
           'grado_pk' : escuela.get('grado_pk'),
           'grado_pke' : escuela.get('grado_pke'),
           'grado_pkm' : escuela.get('grado_pkm'),
           'grado_k' : escuela.get('grado_k'),
           'grado_1' : escuela.get('grado_1'),
           'grado_2' : escuela.get('grado_2'),
           'grado_3' : escuela.get('grado_3'),
           'grado_4' : escuela.get('grado_4'),
           'grado_5' : escuela.get('grado_5'),
           'grado_6' : escuela.get('grado_6'),
           'grado_SGE' : escuela.get('grado_SGE'),
           'grado_7' : escuela.get('grado_7'),
           'grado_8' : escuela.get('grado_8'),
           'grado_9' : escuela.get('grado_9'),
           'grado_SGI' : escuela.get('grado_SGI'),
           'grado_10' : escuela.get('grado_10'),
           'grado_11' : escuela.get('grado_11'),
           'grado_12' : escuela.get('grado_12'),
           'grado_SGS' : escuela.get('grado_SGS'),
           }
           )

    if matricula_created:
        matricula_obj.fecha_creacion = timezone.now
        matricula_obj.fecha_modificacion = timezone.now
        matricula_obj.save()
    else:
        matricula_obj.fecha_modificacion = timezone.now
        matricula_obj.save()


    #Creacion o update de destrezas

    destreza_obj, destreza_created = Destreza.objects.update_or_create(
           escuela = escuela_obj,
           defaults={
           'espanol_prebasico' : escuela.get('espa_ol_pre_b_sico'),
           'espanol_basico' : escuela.get('espa_ol_b_sico'),
           'espanol_proficiente' : escuela.get('espa_ol_proficiente'),
           'espanol_avanzado' : escuela.get('espa_ol_avanzado'),
           'matematicas_prebasico' : escuela.get('matem_ticas_pre_b_sico'),
           'matematicas_basico' : escuela.get('matem_ticas_b_sico'),
           'matematicas_proficiente' : escuela.get('matem_ticas_proficiente'),
           'matematicas_avanzado' : escuela.get('matem_ticas_avanzado'),
           'ingles_prebasico' : escuela.get('ingl_s_pre_b_sico'),
           'ingles_basico' : escuela.get('ingl_s_b_sico'),
           'ingles_proficiente' : escuela.get('ingl_s_proficiente'),
           'ingles_avanzado' : escuela.get('ingl_s_avanzado'),
           }
           )

    if destreza_obj:
        destreza_obj.fecha_creacion = timezone.now
        destreza_obj.fecha_modificacion = timezone.now
        destreza_obj.save()
    else:
        destreza_obj.fecha_modificacion = timezone.now
        destreza_obj.save()
