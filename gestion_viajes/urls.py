from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('crud_alumnos', views.crud_alumnos, name='crud_alumnos'),
    path('alumnosAdd', views.alumnosAdd, name='alumnosAdd'),
    path('alumnos_edit/<str:pk>', views.alumnos_edit, name='alumnos_edit'),
    path('alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),
]
