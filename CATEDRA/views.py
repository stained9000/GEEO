from django.shortcuts import render, get_object_or_404, redirect
from .models import Escuela, Personal, Matricula, Actividad, Destreza, Presupuesto, Visita
from .forms import EscuelaForm, PersonalForm, MatriculaForm, DestrezaForm, ActividadForm, VisitaForm, PresupuestoForm
from django.utils import timezone

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
