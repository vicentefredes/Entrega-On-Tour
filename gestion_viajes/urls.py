from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('crud_colegios', views.crud_colegios, name='crud_colegios'),
    path('colegiosAdd', views.colegiosAdd, name='colegiosAdd'),
    path('colegios_edit/<int:pk>', views.colegios_edit, name='colegios_edit'),
    path('colegios_del/<int:pk>', views.colegios_del, name='colegios_del'),
    path('crud_cursos/<int:fk>', views.crud_cursos, name='crud_cursos'),
    path('cursosAdd/<int:fk>', views.cursosAdd, name='cursosAdd'),
    path('cursos_edit/<int:pk>/<int:fk>', views.cursos_edit, name='cursos_edit'),
    path('cursos_del/<int:pk>', views.cursos_del, name='cursos_del'),
    path('crud_apoderados/<int:fk>/', views.crud_apoderados, name='crud_apoderados'),
    path('apoderadosAdd/<int:fk>', views.apoderadosAdd, name='apoderadosAdd'),
    path('apoderados_edit/<int:pk>', views.apoderados_edit, name='apoderados_edit'),
    path('apoderados_del/<int:pk>', views.apoderados_del, name='apoderados_del'),
    path('crud_alumnos/<int:fk>/', views.crud_alumnos, name='crud_alumnos'),
    path('alumnosAdd/<int:fk>', views.alumnosAdd, name='alumnosAdd'),
    path('alumnos_edit/<int:pk>/<int:fk>', views.alumnos_edit, name='alumnos_edit'),
    path('alumnos_del/<int:pk>', views.alumnos_del, name='alumnos_del'),
]

