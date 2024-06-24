from django.db import models

# Create your models here.
class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)
    
class Nivel(models.Model):
    id_nivel  = models.AutoField(db_column='idNivel', primary_key=True) 
    nivel     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nivel)

class Colegio(models.Model):
    id_colegio  = models.AutoField(db_column='idColegio', primary_key=True) 
    nombre_colegio = models.CharField(max_length=20, blank=False, null=False)
    direccion_colegio = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nombre_colegio)
    
class Curso(models.Model):
    id_curso  = models.AutoField(db_column='idCurso', primary_key=True) 
    id_nivel = models.ForeignKey('Nivel',on_delete=models.CASCADE, db_column='idNivel') 
    letra_curso = models.CharField(max_length=1, blank=False, null=False)
    id_colegio = models.ForeignKey('Colegio',on_delete=models.CASCADE, db_column='idColegio') 

    def __str__(self):
        return str(self.id_nivel) + " " + str(self.letra_curso) + ", " + str(self.id_colegio)

class Apoderado(models.Model):
    id_apoderado        = models.AutoField(db_column='idApoderado', primary_key=True)
    rut              = models.CharField(max_length=10, null=False)
    nombre           = models.CharField(max_length=20, null=False)
    apellido_paterno = models.CharField(max_length=20, null=False)
    apellido_materno = models.CharField(max_length=20, null=False)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    telefono         = models.CharField(max_length=45, null=False)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)+" "+str(self.apellido_materno) 

class Alumno(models.Model):
    id_alumno        = models.AutoField(db_column='idAlumno', primary_key=True)
    rut              = models.CharField(max_length=10, null=False)
    nombre           = models.CharField(max_length=20, null=False)
    apellido_paterno = models.CharField(max_length=20, null=False)
    apellido_materno = models.CharField(max_length=20, null=False)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    telefono         = models.CharField(max_length=45, null=False)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    id_curso         = models.ForeignKey('Curso',on_delete=models.CASCADE, db_column='idCurso')
    id_apoderado     = models.ForeignKey('Apoderado',on_delete=models.CASCADE, db_column='idApoderado')

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)+" "+str(self.apellido_materno) 