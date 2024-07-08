from django.shortcuts import render, redirect
from .models import Nivel, Genero, Colegio, Curso, Alumno, Apoderado, Servicio
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import ColegioForm, CursoForm, AlumnoForm, ApoderadoForm, RegistrationForm, UserUpdateForm, ServicioForm
# Create your views here.

# Inicio
@login_required
def index(request):
    context={'clase':'index'}
    return render(request, 'gestion_viajes/index.html', context)

#CRUD de Usuarios
@login_required
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('crud_usuarios')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form, 'clase':'gestion_usuarios'})

@login_required
def crud_usuarios(request):
    users = User.objects.all().order_by('username') 
    context={'users': users, 'clase':'gestion_usuarios'}
    return render(request, 'gestion_viajes/usuarios_list.html', context)

@login_required
def usuarios_edit(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            mensaje = f"Los datos de {user.username} han sido actualizados exitosamente"
            return render(request, 'gestion_viajes/usuarios_edit.html', {'user': user, 'mensaje': mensaje, 'form': form, 'clase': 'gestion_usuarios'})
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'gestion_viajes/usuarios_edit.html', {'user': user, 'form': form, 'clase': 'gestion_usuarios'})

@login_required
def usuarios_del(request, pk):
    context = {}

    try:
        user = User.objects.get(id=pk)
        user.delete()
        mensaje = f"{user.username} ha sido eliminado"
        users = User.objects.all().order_by('username')
        context = {'mensaje': mensaje, 'users': users, 'clase':'gestion_usuarios'}
        return render(request, 'gestion_viajes/usuarios_list.html', context)
    except:
        mensaje = f"ERROR: el id {pk} no existe"
        users = User.objects.all().order_by('username')
        context = {'mensaje': mensaje, 'users': users, 'clase':'gestion_usuarios'}
        return render(request, 'gestion_viajes/usuarios_list.html', context)

# CRUD de Colegios
@login_required
def crud_colegios(request):
    colegios = Colegio.objects.all().order_by('nombre_colegio')
    context = {'colegios': colegios, 'clase':'gestion_clientes'}
    return render(request, 'gestion_viajes/colegios_list.html', context)

@login_required
def colegiosAdd(request):
    if request.method == "POST":
        form = ColegioForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data.get('nombre_colegio')
            mensaje = f"{nombre} ha sido agregado exitosamente"
            return render(request, 'gestion_viajes/colegios_add.html', {'form': ColegioForm(), 'mensaje': mensaje, 'clase':'gestion_clientes'})
    else:
        form = ColegioForm()
    return render(request, 'gestion_viajes/colegios_add.html', {'form': form, 'clase':'gestion_clientes'})

@login_required
def colegios_edit(request, pk):
    colegio = Colegio.objects.get(id_colegio=pk)
    if request.method == "POST":
        form = ColegioForm(request.POST, instance=colegio)
        if form.is_valid():
            form.save()
            mensaje = f"Los datos de {colegio.nombre_colegio} han sido actualizados exitosamente"
            return render(request, 'gestion_viajes/colegios_edit.html', {'colegio': colegio, 'mensaje': mensaje, 'form': form, 'clase':'gestion_clientes'})
    else:
        form = ColegioForm(instance=colegio)
    return render(request, 'gestion_viajes/colegios_edit.html', {'colegio': colegio, 'form': form, 'clase':'gestion_clientes'})

@login_required
def colegios_del(request, pk):
    context = {}
    try:
        colegio = Colegio.objects.get(id_colegio=pk)
        colegio.delete()
        mensaje = f"{colegio.nombre_colegio} ha sido eliminado"
        context = {'mensaje': mensaje, 'colegios': Colegio.objects.all().order_by('nombre_colegio'), 'clase':'gestion_clientes'}
        return render(request, 'gestion_viajes/colegios_list.html', context)
    except:
        mensaje = f"ERROR: el id {pk} no existe"
        context = {'mensaje': mensaje, 'colegios': Colegio.objects.all().order_by('nombre_colegio'), 'clase':'gestion_clientes'}
        return render(request, 'gestion_viajes/colegios_list.html', context)

# CRUD de Cursos
@login_required
def crud_cursos(request, fk):
    cursos = Curso.objects.filter(id_colegio = fk).order_by('id_nivel', 'letra_curso')
    colegio = Colegio.objects.get(id_colegio=fk)
    context = {'cursos': cursos, 'colegio':colegio, 'clase':'gestion_clientes'}
    return render(request, 'gestion_viajes/cursos_list.html', context)

@login_required
def cursosAdd(request, fk):
    colegio = Colegio.objects.get(id_colegio=fk)
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.id_colegio = colegio
            curso.save()
            mensaje = f"Curso {curso.id_nivel} {curso.letra_curso} ha sido agregado exitosamente"
            return render(request, 'gestion_viajes/cursos_add.html', {'form': CursoForm(), 'mensaje': mensaje, 'colegio': colegio, 'clase':'gestion_clientes'})
    else:
        form = CursoForm()
    return render(request, 'gestion_viajes/cursos_add.html', {'form': form, 'colegio': colegio, 'clase':'gestion_clientes'})

@login_required
def cursos_edit(request, pk, fk):
    colegio = Colegio.objects.get(id_colegio=fk)
    curso = Curso.objects.get(id_curso=pk)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            mensaje = f"Los datos del curso {curso} han sido actualizados exitosamente"
            return render(request, 'gestion_viajes/cursos_edit.html', {'curso': curso, 'mensaje': mensaje, 'form': form, 'colegio': colegio, 'clase':'gestion_clientes'})
    else:
        form = CursoForm(instance=curso)
    return render(request, 'gestion_viajes/cursos_edit.html', {'curso': curso, 'form': form, 'colegio': colegio, 'clase':'gestion_clientes'})

@login_required
def cursos_del(request, pk, fk):
    context = {}

    colegio = Colegio.objects.get(id_colegio=fk)

    try: 
        curso = Curso.objects.get(id_curso=pk)
        curso.delete()
        mensaje = f"Curso {curso} ha sido eliminado"
        cursos = Curso.objects.filter(id_colegio = fk).order_by('id_nivel', 'letra_curso')
        context = {'cursos':cursos, 'mensaje': mensaje, 'colegio':colegio, 'clase':'gestion_clientes'}
        return render(request, 'gestion_viajes/cursos_list.html', context)
    
    except:
        mensaje = f"ERROR: el id {pk} no existe"
        cursos = Curso.objects.filter(id_colegio = fk).order_by('id_nivel', 'letra_curso')
        context = {'cursos':cursos, 'mensaje': mensaje, 'colegio':colegio, 'clase':'gestion_clientes'}
        return render(request, 'gestion_viajes/cursos_list.html', context)
    

# CRUD de Apoderados
@login_required
def crud_apoderados(request, fk):

    curso = Curso.objects.get(id_curso=fk)

    # Obtén todos los alumnos del curso especificado por fk
    alumnos = Alumno.objects.filter(id_curso=fk)
    
    # Obtén los apoderados únicos de estos alumnos
    apoderados_ids = alumnos.values_list('id_apoderado', flat=True).distinct()
    apoderados = Apoderado.objects.filter(id_apoderado__in=apoderados_ids).order_by('apellido_paterno')

    context = {'apoderados': apoderados, 'curso':curso, 'clase':'gestion_clientes'}
    return render(request, 'gestion_viajes/apoderados_list.html', context)

@login_required
def apoderadosAdd(request, fk):
    curso = Curso.objects.get(id_curso=fk)
    if request.method == "POST":
        form = ApoderadoForm(request.POST)
        if form.is_valid():
            apoderado = form.save()
            mensaje = f"{apoderado.nombre} {apoderado.apellido_paterno} ha sido agregado exitosamente"
            return render(request, 'gestion_viajes/apoderados_add.html', {'form': ApoderadoForm(), 'mensaje': mensaje, 'curso': curso, 'clase': 'gestion_clientes'})
    else:
        form = ApoderadoForm()
    return render(request, 'gestion_viajes/apoderados_add.html', {'form': form, 'curso': curso, 'clase': 'gestion_clientes'})


@login_required    
def apoderados_edit(request, pk, fk):
    curso = Curso.objects.get(id_curso=fk)
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
                    context = {'apoderado': apoderado, 'mensaje': mensaje, 'form': form, 'generos': generos, 'curso':curso, 'clase':'gestion_clientes'}
                    return render(request, 'gestion_viajes/apoderados_edit.html', context)
            else:
                form = ApoderadoForm(instance=apoderado)
                mensaje = ""
                context = {'apoderado': apoderado, 'mensaje': mensaje, 'form': form, 'generos': generos, 'curso':curso, 'clase':'gestion_clientes'}
                return render(request, 'gestion_viajes/apoderados_edit.html', context)
    
    except Apoderado.DoesNotExist:
        apoderados = Apoderado.objects.all().order_by('apellido_paterno')
        mensaje = f"ERROR: El apoderado con ID {pk} no existe"
        context = {'apoderados': apoderados, 'mensaje': mensaje, 'clase':'gestion_clientes'}

    return render(request, 'gestion_viajes/apoderados_list.html', context)

@login_required
def apoderados_del(request, pk, fk):
    context = {}

    curso = Curso.objects.get(id_curso=fk)

    try:
        apoderado = Apoderado.objects.get(id_apoderado=pk)
        apoderado.delete()

        if apoderado.id_genero.genero == "Masculino":
            mensaje = f"{apoderado.nombre} {apoderado.apellido_paterno} {apoderado.apellido_materno} ha sido eliminado"
        else:
            mensaje = f"{apoderado.nombre} {apoderado.apellido_paterno} {apoderado.apellido_materno} ha sido eliminada"

        # Obtén todos los alumnos del curso especificado por fk
        alumnos = Alumno.objects.filter(id_curso=fk)
        
        # Obtén los apoderados únicos de estos alumnos
        apoderados_ids = alumnos.values_list('id_apoderado', flat=True).distinct()
        apoderados = Apoderado.objects.filter(id_apoderado__in=apoderados_ids).order_by('apellido_paterno')

        context = {'apoderados': apoderados, 'mensaje': mensaje,'curso':curso, 'clase':'gestion_clientes'}
        return render(request, 'gestion_viajes/apoderados_list.html', context)
    
    except:
        mensaje = f"ERROR: el rut {pk} no existe"
        # Obtén todos los alumnos del curso especificado por fk
        alumnos = Alumno.objects.filter(id_curso=fk)
        
        # Obtén los apoderados únicos de estos alumnos
        apoderados_ids = alumnos.values_list('id_apoderado', flat=True).distinct()
        apoderados = Apoderado.objects.filter(id_apoderado__in=apoderados_ids).order_by('apellido_paterno')
        context = {'apoderados': apoderados, 'mensaje': mensaje, 'curso':curso, 'clase':'gestion_clientes'}
        return render(request, 'gestion_viajes/apoderados_list.html', context)
    
# CRUD de alumnos
@login_required
def crud_alumnos(request, fk):
    alumnos = Alumno.objects.filter(id_curso = fk).order_by('apellido_paterno')
    curso = Curso.objects.get(id_curso=fk)
    context = {'alumnos':alumnos, 'curso':curso, 'clase':'gestion_clientes'}
    return render(request, 'gestion_viajes/alumnos_list.html', context)

@login_required
def alumnosAdd(request, fk):
    curso = Curso.objects.get(id_curso=fk)
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.id_curso = curso
            alumno.save()
            nombre = form.cleaned_data.get('nombre')
            apaterno = form.cleaned_data.get('apellido_paterno')
            amaterno = form.cleaned_data.get('apellido_materno')
            id_genero = form.cleaned_data.get('id_genero')
            objGenero = Genero.objects.get(id_genero=id_genero.id_genero)
            
            if objGenero.genero == 'Masculino':
                mensaje = f"{nombre} {apaterno} {amaterno} ha sido agregado exitosamente"
            else:
                mensaje = f"{nombre} {apaterno} {amaterno} ha sido agregada exitosamente"
            
            return render(request, 'gestion_viajes/alumnos_add.html', {'form': AlumnoForm(), 'mensaje': mensaje, 'curso':curso, 'clase':'gestion_clientes'})
    else:
        form = AlumnoForm()
    
    return render(request, 'gestion_viajes/alumnos_add.html', {'form': form, 'curso':curso, 'clase':'gestion_clientes'})

@login_required   
def alumnos_edit(request, pk, fk):
    curso = Curso.objects.get(id_curso=fk)
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
                    context = {'alumno': alumno, 'mensaje': mensaje, 'form': form, 'generos': generos, 'curso':curso, 'clase':'gestion_clientes'}
                    return render(request, 'gestion_viajes/alumnos_edit.html', context)
            
            else:
                form = AlumnoForm(instance=alumno)
                mensaje = ""
                context = {'alumno': alumno, 'mensaje': mensaje, 'form': form, 'generos': generos, 'curso':curso, 'clase':'gestion_clientes'}
                return render(request, 'gestion_viajes/alumnos_edit.html', context)
    
    except Alumno.DoesNotExist:
        alumnos = Alumno.objects.filter(id_curso = fk).order_by('apellido_paterno')
        mensaje = f"ERROR: El alumno con ID {pk} no existe"
        context = {'alumnos': alumnos, 'mensaje': mensaje, 'curso':curso, 'clase':'gestion_clientes'}

    return render(request, 'gestion_viajes/alumnos_list.html', context)

@login_required
def alumnos_del(request, pk, fk):
    context = {}

    curso = Curso.objects.get(id_curso=fk)

    try:
        alumno = Alumno.objects.get(id_alumno=pk)
        alumno.delete()

        if alumno.id_genero.genero == "Masculino":
            mensaje = f"{alumno.nombre} {alumno.apellido_paterno} {alumno.apellido_materno} ha sido eliminado"
        else:
            mensaje = f"{alumno.nombre} {alumno.apellido_paterno} {alumno.apellido_materno} ha sido eliminada"

        alumnos = Alumno.objects.filter(id_curso = fk).order_by('apellido_paterno')
        context = {'alumnos': alumnos, 'mensaje': mensaje, 'curso':curso, 'clase':'gestion_clientes'}
        return render(request, 'gestion_viajes/alumnos_list.html', context)
    
    except:
        mensaje = f"ERROR: el rut {pk} no existe"
        alumnos = Alumno.objects.filter(id_curso = fk).order_by('apellido_paterno')
        context = {'alumnos': alumnos, 'mensaje': mensaje, 'curso':curso, 'clase':'gestion_clientes'}
        return render(request, 'gestion_viajes/alumnos_list.html', context)
    
@login_required
def crud_servicios(request):
    servicios = Servicio.objects.all().order_by('descripcion_servicio')
    context = {'servicios': servicios, 'clase':'gestion_contratos'}
    return render(request, 'gestion_viajes/servicios_list.html', context)

@login_required
def servicios_add(request):
    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            descripcion = form.cleaned_data.get('descripcion_servicio')
            mensaje = f"{descripcion} ha sido agregado exitosamente"
            return render(request, 'gestion_viajes/servicios_add.html', {'form': ServicioForm(), 'mensaje': mensaje, 'clase':'gestion_contratos'})
    else:
        form = ServicioForm()
    return render(request, 'gestion_viajes/servicios_add.html', {'form': form, 'clase':'gestion_contratos'})

@login_required
def servicios_edit(request, pk):
    servicio = Servicio.objects.get(id_servicio=pk)
    if request.method == "POST":
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            mensaje = f"Los datos de {servicio.descripcion_servicio} han sido actualizados exitosamente"
            return render(request, 'gestion_viajes/servicios_edit.html', {'servicio': servicio, 'mensaje': mensaje, 'form': form, 'clase':'gestion_contratos'})
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'gestion_viajes/servicios_edit.html', {'servicio': servicio, 'form': form, 'clase':'gestion_contratos'})

@login_required
def servicios_del(request, pk):
    context = {}
    try:
        servicio = Servicio.objects.get(id_servicio=pk)
        servicio.delete()
        mensaje = f"{servicio.descripcion_servicio} ha sido eliminado"
        context = {'mensaje': mensaje, 'servicios': Servicio.objects.all().order_by('descripcion_servicio'), 'clase':'gestion_contratos'}
        return render(request, 'gestion_viajes/servicios_list.html', context)
    except Servicio.DoesNotExist:
        mensaje = f"ERROR: el id {pk} no existe"
        context = {'mensaje': mensaje, 'servicios': Servicio.objects.all().order_by('descripcion_servicio'), 'clase':'gestion_contratos'}
        return render(request, 'gestion_viajes/servicios_list.html', context)

