# Generated by Django 4.1.2 on 2024-06-24 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colegio',
            fields=[
                ('id_colegio', models.AutoField(db_column='idColegio', primary_key=True, serialize=False)),
                ('nombre_colegio', models.CharField(max_length=20)),
                ('direccion_colegio', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id_nivel', models.AutoField(db_column='idNivel', primary_key=True, serialize=False)),
                ('nivel', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.AutoField(db_column='idCurso', primary_key=True, serialize=False)),
                ('letra_curso', models.CharField(max_length=1)),
                ('id_colegio', models.ForeignKey(db_column='idColegio', on_delete=django.db.models.deletion.CASCADE, to='gestion_viajes.colegio')),
                ('id_nivel', models.ForeignKey(db_column='idNivel', on_delete=django.db.models.deletion.CASCADE, to='gestion_viajes.nivel')),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id_alumno', models.AutoField(db_column='idAlumno', primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=20)),
                ('apellido_materno', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=45)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('id_curso', models.ForeignKey(db_column='idCurso', on_delete=django.db.models.deletion.CASCADE, to='gestion_viajes.curso')),
                ('id_genero', models.ForeignKey(db_column='idGenero', on_delete=django.db.models.deletion.CASCADE, to='gestion_viajes.genero')),
            ],
        ),
    ]
