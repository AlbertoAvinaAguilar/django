from django.db import models

# Create your models here.
class Usuarios(models.Model): #Debe de coincidir exactamente con el nombre de la tabla de la base de datos
    iduser = models.BigIntegerField(db_column='idUser')  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(db_column='apellido_paterno', max_length=50)  # Field renamed to remove unsuitable characters.
    apellido_materno = models.CharField(db_column='apellido_materno', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    
class Departamento(models.Model):
    iddepartamento = models.CharField(db_column='idDepartamento', max_length=8, primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'departamento'    