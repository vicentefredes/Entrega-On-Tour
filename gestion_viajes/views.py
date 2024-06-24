from django.shortcuts import render
from .models import Nivel, Genero, Colegio, Curso, Alumno, Apoderado
from django.contrib.auth.decorators import login_required

from .forms import ColegioForm, CursoForm, AlumnoForm, ApoderadoForm
# Create your views here.

def index(request):
    context={}
    return render(request, 'gestion_viajes/index.html', context)

# CRUD de Colegios
def crud_colegios(request):
    colegios = Colegio.objects.all().order_by('nombre_colegio')
    context = {'colegios': colegios}
    return render(request, 'gestion_viajes/colegios_list.html', context)

def colegiosAdd(request):
    if request.method == "POST":
        form = ColegioForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data.get('nombre_colegio')
            mensaje = f"{nombre} ha sido agregado exitosamente"
            return render(request, 'gestion_viajes/colegios_add.html', {'form': ColegioForm(), 'mensaje': mensaje})
    else:
        form = ColegioForm()
    return render(request, 'gestion_viajes/colegios_add.html', {'form': form})

def colegios_edit(request, pk):
    colegio = Colegio.objects.get(id_colegio=pk)
    if request.method == "POST":
        form = ColegioForm(request.POST, instance=colegio)
        if form.is_valid():
            form.save()
            mensaje = f"Los datos de {colegio.nombre_colegio} han sido actualizados exitosamente"
            return render(request, 'gestion_viajes/colegios_edit.html', {'colegio': colegio, 'mensaje': mensaje, 'form': form})
    else:
        form = ColegioForm(instance=colegio)
    return render(request, 'gestion_viajes/colegios_edit.html', {'colegio': colegio, 'form': form})

def colegios_del(request, pk):
    colegio = Colegio.objects.get(id_colegio=pk)
    if request.method == "POST":
        colegio.delete()
        mensaje = f"{colegio.nombre_colegio} ha sido eliminado"
        return render(request, 'gestion_viajes/colegios_list.html', {'mensaje': mensaje, 'colegios': Colegio.objects.all().order_by('nombre_colegio')})
    return render(request, 'gestion_viajes/colegios_del.html', {'colegio': colegio})

# CRUD de Cursos
def crud_cursos(request):
    cursos = Curso.objects.all().order_by('id_nivel', 'letra_curso')
    context = {'cursos': cursos}
    return render(request, 'gestion_viajes/cursos_list.html', context)

def cursosAdd(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            curso = form.cleaned_data.get('id_nivel')
            mensaje = f"Curso {curso} ha sido agregado exitosamente"
            return render(request, 'gestion_viajes/cursos_add.html', {'form': CursoForm(), 'mensaje': mensaje})
    else:
        form = CursoForm()
    return render(request, 'gestion_viajes/cursos_add.html', {'form': form})

def cursos_edit(request, pk):
    curso = Curso.objects.get(id_curso=pk)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            mensaje = f"Los datos del curso {curso} han sido actualizados exitosamente"
            return render(request, 'gestion_viajes/cursos_edit.html', {'curso': curso, 'mensaje': mensaje, 'form': form})
    else:
        form = CursoForm(instance=curso)
    return render(request, 'gestion_viajes/cursos_edit.html', {'curso': curso, 'form': form})

def cursos_del(request, pk):
    curso = Curso.objects.get(id_curso=pk)
    if request.method == "POST":
        curso.delete()
        mensaje = f"Curso {curso} ha sido eliminado"
        return render(request, 'gestion_viajes/cursos_list.html', {'mensaje': mensaje, 'cursos': Curso.objects.all().order_by('id_nivel', 'letra_curso')})
    return render(request, 'gestion_viajes/cursos_del.html', {'curso': curso})

# CRUD de Apoderados
def crud_apoderados(request):
    apoderados = Apoderado.objects.all().order_by('apellido_paterno')
    context = {'apoderados': apoderados}
    return render(request, 'gestion_viajes/apoderados_list.html', context)

def apoderadosAdd(request):
    if request.method == "POST":
        form = ApoderadoForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data.get('nombre')
            apaterno = form.cleaned_data.get('apellido_paterno')
            amaterno = form.cleaned_data.get('apellido_materno')
            id_genero = form.cleaned_data.get('id_genero')
            objGenero = id_genero
            if objGenero.genero == 'Masculino':
                mensaje = f"{nombre} {apaterno} {amaterno} ha sido agregado exitosamente"
            else:
                mensaje = f"{nombre} {apaterno} {amaterno} ha sido agregada exitosamente"
            return render(request, 'gestion_viajes/apoderados_add.html', {'form': ApoderadoForm(), 'mensaje': mensaje})
    else:
        form = ApoderadoForm()
    return render(request, 'gestion_viajes/apoderados_add.html', {'form': form})
    
def apoderados_edit(request, pk):
    try:
        apoderado = Apoderado.objects.get(id_apoderado=pk)
        generos = Genero.objects.all()
        context = {}
        if apoderado:
            if request.method == "POST":
                form = ApoderadoForm(request.POST, instance=apoderado)
                if form.is_valid():
                    form.save()
                    mensaje = f"Los datos de {apoderado.nombre} {apoderado.apellido_paterno} {apoderado.apellido_materno} han sido actualizados exitosamente"
                    context = {'apoderado': apoderado, 'mensaje': mensaje, 'form': form, 'generos': generos}
                    return render(request, 'gestion_viajes/apoderados_edit.html', context)
            else:
                form = ApoderadoForm(instance=apoderado)
                mensaje = ""
                context = {'apoderado': apoderado, 'mensaje': mensaje, 'form': form, 'generos': generos}
                return render(request, 'gestion_viajes/apoderados_edit.html', context)
    
    except Apoderado.DoesNotExist:
        apoderados = Apoderado.objects.all().order_by('apellido_paterno')
        mensaje = f"ERROR: El apoderado con ID {pk} no existe"
        context = {'apoderados': apoderados, 'mensaje': mensaje}

    return render(request, 'gestion_viajes/apoderados_list.html', context)

def apoderados_del(request, pk):
    context = {}
    try:
        apoderado = Apoderado.objects.get(id_apoderado=pk)
        apoderado.delete()
        if apoderado.id_genero.genero == "Masculino":
            mensaje = f"{apoderado.nombre} {apoderado.apellido_paterno} {apoderado.apellido_materno} ha sido eliminado"
        else:
            mensaje = f"{apoderado.nombre} {apoderado.apellido_paterno} {apoderado.apellido_materno} ha sido eliminada"
        apoderados = Apoderado.objects.all().order_by('apellido_paterno')
        context = {'apoderados': apoderados, 'mensaje': mensaje}
        return render(request, 'gestion_viajes/apoderados_list.html', context)
    
    except:
        mensaje = f"ERROR: el rut {pk} no existe"
        apoderados = Apoderado.objects.all().order_by('apellido_paterno')
        context = {'apoderados': apoderados, 'mensaje': mensaje}
        return render(request, 'gestion_viajes/apoderados_list.html', context)

# CRUD de alumnos
def crud_alumnos(request):
    alumnos = Alumno.objects.all().order_by('apellido_paterno')
    context = {'alumnos':alumnos}
    return render(request, 'gestion_viajes/alumnos_list.html', context)

def alumnosAdd(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data.get('nombre')
            apaterno = form.cleaned_data.get('apellido_paterno')
            amaterno = form.cleaned_data.get('apellido_materno')
            id_genero = form.cleaned_data.get('id_genero')
            objGenero = Genero.objects.get(id_genero=id_genero.id_genero)
            
            if objGenero.genero == 'Masculino':
                mensaje = f"{nombre} {apaterno} {amaterno} ha sido agregado exitosamente"
            else:
                mensaje = f"{nombre} {apaterno} {amaterno} ha sido agregada exitosamente"
            
            return render(request, 'gestion_viajes/alumnos_add.html', {'form': AlumnoForm(), 'mensaje': mensaje})
    else:
        form = AlumnoForm()
    
    return render(request, 'gestion_viajes/alumnos_add.html', {'form': form})
    
def alumnos_edit(request, pk):
    try:
        alumno = Alumno.objects.get(id_alumno=pk)
        generos = Genero.objects.all()

        context = {}

        if alumno:
            if request.method == "POST":
                form = AlumnoForm(request.POST, instance=alumno)
                if form.is_valid():
                    form.save()
                    mensaje = f"Los datos de {alumno.nombre} {alumno.apellido_paterno} {alumno.apellido_materno} han sido actualizados exitosamente"
                    context = {'alumno': alumno, 'mensaje': mensaje, 'form': form, 'generos': generos}
                    return render(request, 'gestion_viajes/alumnos_edit.html', context)
            
            else:
                form = AlumnoForm(instance=alumno)
                mensaje = ""
                context = {'alumno': alumno, 'mensaje': mensaje, 'form': form, 'generos': generos}
                return render(request, 'gestion_viajes/alumnos_edit.html', context)
    
    except Alumno.DoesNotExist:
        alumnos = Alumno.objects.all().order_by('apellido_paterno')
        mensaje = f"ERROR: El alumno con ID {pk} no existe"
        context = {'alumnos': alumnos, 'mensaje': mensaje}

    return render(request, 'gestion_viajes/alumnos_list.html', context)


def alumnos_del(request, pk):
    context = {}

    try:
        alumno = Alumno.objects.get(id_alumno=pk)

        alumno.delete()

        if alumno.id_genero.genero == "Masculino":
            mensaje = f"{alumno.nombre} {alumno.apellido_paterno} {alumno.apellido_materno} ha sido eliminado"
        else:
            mensaje = f"{alumno.nombre} {alumno.apellido_paterno} {alumno.apellido_materno} ha sido eliminada"

        alumnos = Alumno.objects.all().order_by('apellido_paterno')
        context = {'alumnos': alumnos, 'mensaje': mensaje}
        return render(request, 'gestion_viajes/alumnos_list.html', context)
    
    except:
        mensaje = f"ERROR: el rut {pk} no existe"
        alumnos = Alumno.objects.all().order_by('apellido_paterno')
        context = {'alumnos': alumnos, 'mensaje': mensaje}
        return render(request, 'gestion_viajes/alumnos_list.html', context)