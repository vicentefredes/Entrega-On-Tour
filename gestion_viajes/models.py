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
    id_apoderado     = models.AutoField(db_column='idApoderado', primary_key=True)
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
    
class Proveedor(models.Model):
    id_proveedor     = models.AutoField(db_column='idProveedor', primary_key=True)
    nombre_proveedor = models.CharField(max_length=30, null=False)
    email_proveedor  = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    telefono         = models.CharField(max_length=45, null=True)

    def __str__(self):
        return str(self.nombre_proveedor)

class TipoServicio(models.Model):
    id_tiposervicio = models.AutoField(db_column='idTipoServicio', primary_key=True)
    descripcion_tiposervicio = models.CharField(max_length=30, null=False)

    def __str__(self):
        return str(self.descripcion_tiposervicio)

class Destino (models.Model):
    id_destino = models.AutoField(db_column='idDestino', primary_key=True)
    nombre_destino = models.CharField(max_length=100, null=False)

    def __str__(self):
        return str(self.nombre_destino)
class Servicio(models.Model):
    id_servicio = models.AutoField(db_column='idServicio', primary_key=True)
    descripcion_servicio = models.CharField(max_length=50, null=False)
    id_tiposervicio = models.ForeignKey('TipoServicio',on_delete=models.CASCADE, db_column='idTipoServicio')  
    id_proveedor = models.ForeignKey('Proveedor',on_delete=models.CASCADE, db_column='idProveedor')
    id_destino = models.ForeignKey('Destino',on_delete=models.CASCADE, db_column='idDestino')
    precio_servicio = models.IntegerField(null=False)

    def __str__(self):
        return str(self.descripcion_servicio)