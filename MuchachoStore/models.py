from django.db import models

# Create your models here.
# Modelo par genero

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True, db_column='Genero')
    nombre = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.nombre)


# Modelo para usuario

class Usuario(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(blank=True, null=False)
    idGenero = models.ForeignKey(Genero, on_delete=models.CASCADE, db_column='Genero')
    correo = models.EmailField()
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)


    def __str__(self):
        return str(self.rut) + " " + str(self.nombre) + " " + str(self.apellido_paterno) + " " + str(self.apellido_materno) + " " + str(self.fecha_nacimiento) + " " + str(self.idGenero) + " " + str(self.correo) + " " + str(self.telefono) + " " + str(self.direccion) + " " + str(self.contrasena) + " " + str(self.activo)
