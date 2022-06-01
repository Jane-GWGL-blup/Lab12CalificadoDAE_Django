from django.db import models

# Create your models here.
class Libro(models.Model):
    codigo = models.IntegerField(default=0, unique=True)
    titulo = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=30)
    editorial = models.CharField(max_length=60)
    NumPags = models.IntegerField()

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

class Usuario(models.Model):
    numUsuario = models.IntegerField(default=0,unique=True)
    NIF = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

class Prestamos(models.Model):
    idLibro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecPrestamo= models.DateField()
    fecDevolucion= models.DateField()

