from django import forms
from .models import Colegio, Curso, Alumno

from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm

class ColegioForm(ModelForm):
    class Meta:
        model = Colegio
        fields = ['nombre_colegio', 'direccion_colegio']
        labels = {'nombre_colegio': 'Nombre',
                  'creditos': 'Dirección'}
        widgets = {
            'nombre_colegio': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_colegio': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['id_nivel', 'letra_curso', 'id_colegio']
        labels = {'id_nivel': "Curso", 
                  'letra_curso': "",
                  'id_colegio': "Colegio"}
        widgets = {
            'id_nivel': forms.Select(attrs={'class': 'form-control'}),
            'letra_curso': forms.TextInput(attrs={'class': 'form-control'}),
            'id_colegio': forms.Select(attrs={'class': 'form-control'}),
        }

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = [
            'rut', 'nombre', 'apellido_paterno', 'apellido_materno', 
            'fecha_nacimiento', 'id_genero', 'telefono', 'email', 
            'direccion', 'id_curso'
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
            'id_curso': "Curso",
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
            'id_curso': forms.Select(attrs={'class': 'form-control'}),
        }