from django import forms
from .models import Colegio, Curso, Alumno, Apoderado, Servicio

from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Requerido. Ingresa una dirección de correo válida.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }
        help_texts = {
            'username': 'Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ únicamente.',
        }
class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }
class ColegioForm(ModelForm):
    class Meta:
        model = Colegio
        fields = ['nombre_colegio', 'direccion_colegio']
        labels = {'nombre_colegio': 'Nombre',
                  'direccion_colegio': 'Dirección'}
        widgets = {
            'nombre_colegio': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_colegio': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        exclude = ['id_colegio']
        fields = ['id_nivel', 'letra_curso']
        labels = {'id_nivel': "Nivel", 
                  'letra_curso': "Curso"}
        widgets = {
            'id_nivel': forms.Select(attrs={'class': 'form-control'}),
            'letra_curso': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ApoderadoForm(forms.ModelForm):
    class Meta:
        model = Apoderado
        fields = [
            'rut', 'nombre', 'apellido_paterno', 'apellido_materno',
            'fecha_nacimiento', 'id_genero', 'telefono', 'email', 'direccion'
        ]
        labels = {
            'rut': "RUT",
            'nombre': "Nombre",
            'apellido_paterno': "Apellido Paterno",
            'apellido_materno': "Apellido Materno",
            'fecha_nacimiento': "Fecha de Nacimiento",
            'id_genero': "Género",
            'telefono': "Teléfono",
            'email': "Email",
            'direccion': "Dirección",
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'id_genero': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        exclude = ['id_curso']
        fields = [
            'rut', 'nombre', 'apellido_paterno', 'apellido_materno', 
            'fecha_nacimiento', 'id_genero', 'telefono', 'email', 
            'direccion', 'id_apoderado'
        ]
        labels = {
            'rut': "RUT",
            'nombre': "Nombre",
            'apellido_paterno': "Apellido Paterno",
            'apellido_materno': "Apellido Materno",
            'fecha_nacimiento': "Fecha de Nacimiento",
            'id_genero': "Género",
            'telefono': "Teléfono",
            'email': "Email",
            'direccion': "Dirección",
            'id_apoderado': 'Apoderado',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'id_genero': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'id_apoderado': forms.Select(attrs={'class': 'form-control'}),
        }

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = ['descripcion_servicio', 'id_tiposervicio', 'id_proveedor', 'id_destino', 'precio_servicio']
        labels = {
            'descripcion_servicio': 'Descripción del Servicio',
            'id_tiposervicio': 'Tipo de Servicio',
            'id_proveedor': 'Proveedor',
            'id_destino': 'Destino',
            'precio_servicio': 'Precio',
        }
        widgets = {
            'descripcion_servicio': forms.TextInput(attrs={'class': 'form-control'}),
            'id_tiposervicio': forms.Select(attrs={'class': 'form-control'}),
            'id_proveedor': forms.Select(attrs={'class': 'form-control'}),
            'id_destino': forms.Select(attrs={'class': 'form-control'}),
            'precio_servicio': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        