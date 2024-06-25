from django import forms
from .models import Colegio, Curso, Alumno, Apoderado

from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm

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

        