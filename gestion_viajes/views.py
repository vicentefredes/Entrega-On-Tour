from django.shortcuts import render
from .models import Nivel, Genero, Colegio, Curso, Alumno
from django.contrib.auth.decorators import login_required

from .forms import ColegioForm, CursoForm, AlumnoForm
# Create your views here.

def index(request):
    context={}
    return render(request, 'gestion_viajes/index.html', context)

#ALUMNOS
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