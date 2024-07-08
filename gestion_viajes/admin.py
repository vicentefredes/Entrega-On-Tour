from django.contrib import admin
from .models import Genero, Nivel, Colegio, Curso, Alumno, Apoderado, Proveedor, TipoServicio, Destino, Servicio

admin.site.register(Genero)
admin.site.register(Nivel)
admin.site.register(Colegio)
admin.site.register(Curso)
admin.site.register(Apoderado)
admin.site.register(Alumno)
admin.site.register(Proveedor)
admin.site.register(TipoServicio)
admin.site.register(Destino)
admin.site.register(Servicio)