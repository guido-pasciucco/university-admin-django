from django.db import models

# Create your models here.
class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

class Estudiante(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    generos = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('X', 'No Binario')
    ]
    genero = models.CharField(max_length=1, choices=generos, default='F')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    regularidad = models.BooleanField(default=True)

    def nombre_completo(self):
        texto = "{0}, {1}"
        return texto.format(self.apellidos, self.nombres)

class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fecha_matricula = models.DateTimeField(auto_now_add=True)