from django.shortcuts import render, get_object_or_404, redirect
from .models import Escuela, Personal, Matricula, Actividad, Destreza, Presupuesto, Visita
from .forms import EscuelaForm, PersonalForm, MatriculaForm, DestrezaForm, ActividadForm, VisitaForm, PresupuestoForm
from django.utils import timezone
from sodapy import Socrata

# Create your views here.
def lista_escuelas(request):

    escuelas = Escuela.objects.all()
    return render(request, 'CATEDRA/lista_escuelas.html', {'escuelas': escuelas})

def inicio(request):

    return render(request, 'CATEDRA/inicio.html')

def perfil_escuela(request, codigo):

    escuela = get_object_or_404(Escuela, codigo=codigo)

    try:
        personal = Personal.objects.get(escuela=escuela)
    except:
        personal = 'Aún no se ha agregado información de personal administrativo a esta escuela.'

    try:
        matricula = Matricula.objects.get(escuela=escuela)

        total_maestros = matricula.maestros_de_espanol + matricula.maestros_de_matematicas + matricula.maestros_de_ingles + matricula.maestros_de_ciencias + matricula.maestros_otros
    except:
        matricula = 'Aún no se ha agregado información de matrícula a esta escuela.'

        total_maestros = None

    try:
        destrezas = Destreza.objects.get(escuela=escuela)
    except:
        destrezas = 'Aún no se ha agregado información de destrezas a esta escuela.'


    actividades = Actividad.objects.filter(escuela=escuela)

    if len(actividades) == 0:
        actividades = 'Aún no se ha agregado información de actividades a esta escuela.'


    return render(request, 'CATEDRA/perfil_escuela.html', {'escuela': escuela, 'personal': personal, 'matricula': matricula, 'total_maestros': total_maestros, 'destrezas': destrezas, 'actividades': actividades})

def crear_escuela(request):
    if request.method == "POST":
        form = EscuelaForm(request.POST)
        if form.is_valid():
            escuela = form.save(commit=False)
            escuela.author = request.user
            escuela.fecha_creacion = timezone.now()
            escuela.save()
            return redirect('perfil_escuela', codigo=escuela.codigo)
    else:
        form = EscuelaForm()

    return render(request, 'CATEDRA/escuela_edit.html', {'form': form})

def escuela_edit(request, codigo):
    escuela = get_object_or_404(Escuela, codigo=codigo)
    if request.method == "POST":
        form = EscuelaForm(request.POST, instance=escuela)
        if form.is_valid():
            escuela = form.save(commit=False)
            escuela.author = request.user
            escuela.fecha_creacion = timezone.now()
            escuela.save()
            return redirect('perfil_escuela', codigo=escuela.codigo)
    else:
        form = EscuelaForm(instance=escuela)

    return render(request, 'CATEDRA/escuela_edit.html', {'form': form})

def crear_personal(request, codigo):
    escuela = Escuela.objects.get(codigo=codigo)
    if request.method == "POST":
        form = PersonalForm(request.POST)
        if form.is_valid():
            personal = form.save(commit=False)
            personal.escuela = escuela
            personal.fecha_modificacion = timezone.now()
            personal.save()
            return redirect('perfil_escuela', codigo=codigo)
    else:
        form = PersonalForm()

    return render(request, 'CATEDRA/personal_edit.html', {'form': form, 'escuela': escuela})

def personal_edit(request, codigo):
    escuela = Escuela.objects.get(codigo=codigo)
    personal = get_object_or_404(Personal, escuela=escuela)
    if request.method == "POST":
        form = PersonalForm(request.POST, instance=personal)
        if form.is_valid():
            personal = form.save(commit=False)
            personal.fecha_modificacion = timezone.now()
            personal.save()
            return redirect('perfil_escuela', codigo=codigo)
    else:
        form = PersonalForm(instance=personal)

    return render(request, 'CATEDRA/personal_edit.html', {'form': form, 'escuela': escuela})

def crear_matricula(request, codigo):
    if request.method == "POST":
        form = MatriculaForm(request.POST)
        if form.is_valid():
            matricula = form.save(commit=False)
            matricula.escuela = Escuela.objects.get(codigo=codigo)
            matricula.fecha_modificacion = timezone.now()
            matricula.save()
            return redirect('perfil_escuela', codigo=codigo)
    else:
        form = MatriculaForm()

    return render(request, 'CATEDRA/matricula_edit.html', {'form': form})

def matricula_edit(request, codigo):
    matricula = get_object_or_404(Matricula, escuela=Escuela.objects.get(codigo=codigo))
    if request.method == "POST":
        form = MatriculaForm(request.POST, instance=matricula)
        if form.is_valid():
            matricula = form.save(commit=False)
            matricula.fecha_modificacion = timezone.now()
            matricula.save()
            return redirect('perfil_escuela', codigo=codigo)
    else:
        form = MatriculaForm(instance=matricula)

    return render(request, 'CATEDRA/matricula_edit.html', {'form': form})

def crear_destrezas(request, codigo):
    escuela = Escuela.objects.get(codigo=codigo)
    if request.method == "POST":
        form = DestrezaForm(request.POST)
        if form.is_valid():
            destrezas = form.save(commit=False)
            destrezas.escuela = escuela
            destrezas.fecha_modificacion = timezone.now()
            destrezas.save()
            return redirect('perfil_escuela', codigo=codigo)
    else:
        form = DestrezaForm()

    return render(request, 'CATEDRA/destrezas_edit.html', {'form': form, 'escuela': escuela})

def destrezas_edit(request, codigo):
    escuela = Escuela.objects.get(codigo=codigo)
    destrezas = get_object_or_404(Destreza, escuela=Escuela.objects.get(codigo=codigo))
    if request.method == "POST":
        form = DestrezaForm(request.POST, instance=destrezas)
        if form.is_valid():
            destrezas = form.save(commit=False)
            destrezas.fecha_modificacion = timezone.now()
            destrezas.save()
            return redirect('perfil_escuela', codigo=codigo)
    else:
        form = MatriculaForm(instance=destrezas)

    return render(request, 'CATEDRA/destrezas_edit.html', {'form': form, 'escuela': escuela})

def crear_actividad(request, codigo):
    if request.method == "POST":
        form = ActividadForm(request.POST)
        if form.is_valid():
            actividad = form.save(commit=False)
            actividad.escuela = Escuela.objects.get(codigo=codigo)
            actividad.usuario = request.user
            actividad.fecha_creacion = timezone.now()
            actividad.save()
            return redirect('perfil_escuela', codigo=codigo)
    else:
        form = ActividadForm()

    return render(request, 'CATEDRA/actividad_edit.html', {'form': form})

def actividad_edit(request, codigo, pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    if request.method == "POST":
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            actividad = form.save(commit=False)
            actividad.usuario = request.user
            actividad.fecha_modificacion = timezone.now()
            actividad.save()
            return redirect('perfil_escuela', codigo=codigo)
    else:
        form = ActividadForm(instance=actividad)

    return render(request, 'CATEDRA/actividad_edit.html', {'form': form})


def cargar_escuelas(request):
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
        #Filtro de codigos de escuelas invalidos
        try:
            int(escuela['codigo'])
        except:
            continue

        #Creacion o update de escuelas
        escuela_obj, escuela_created = Escuela.objects.update_or_create(
                codigo = escuela['codigo'],
                defaults={
                'nombre': escuela['escuela'],
                'telefono': '(787) ' + escuela.get('telefono', '000-0000'),
                'fax' : '(787) ' + escuela.get('fax', '000-0000'),
                'region_educativa' : escuela['region'],
                'distrito_escolar' : escuela['distrito'],
                'municipio_escolar' : escuela.get('municipio_escolar'),
                'direccion_fisica' : escuela.get('direccio_fisica'),
                'direccion_zipcode' : escuela.get('direccion_zipcode'),
                'zona' : escuela.get('zona', "RURAL"),
                'operacional' : escuela['estatus_actual'],
                'nivel' : escuela.get('nivel_original', 'Elemental'),
                'grados' : escuela.get('grados_posterior'),
                }
                )

        if escuela_created:
            escuela_obj.fecha_creacion = timezone.now()
            escuela_obj.fecha_modificacion = timezone.now()
            escuela_obj.save()
        else:
            escuela_obj.fecha_modificacion = timezone.now()
            escuela_obj.save()


        #Creacion o update de personal de las Escuelas
        #La data solo contiene informacion del director. La otra debe ser llenada manual.

        personal_obj, personal_created = Personal.objects.update_or_create(
               escuela = escuela_obj,
               defaults={
               'nombre_del_director' : escuela.get('director'),
               }
               )

        if personal_created:
            personal_obj.fecha_creacion = timezone.now()
            personal_obj.fecha_modificacion = timezone.now()
            personal_obj.save()
        else:
            personal_obj.fecha_modificacion = timezone.now()
            personal_obj.save()


        #Creacion o update de matricula de la escuela

        matricula_obj, matricula_created = Matricula.objects.update_or_create(
               escuela = escuela_obj,
               defaults={
               'matricula_de_estudiantes' : escuela.get('matricula_total'),
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
            matricula_obj.fecha_creacion = timezone.now()
            matricula_obj.fecha_modificacion = timezone.now()
            matricula_obj.save()
        else:
            matricula_obj.fecha_modificacion = timezone.now()
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
            destreza_obj.fecha_creacion = timezone.now()
            destreza_obj.fecha_modificacion = timezone.now()
            destreza_obj.save()
        else:
            destreza_obj.fecha_modificacion = timezone.now()
            destreza_obj.save()

    return render(request, 'CATEDRA/cargar_escuelas.html', {})
