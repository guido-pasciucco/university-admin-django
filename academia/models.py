from django.db import models

class Persona(models.Model):
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
    def nombre_completo(self):
        return f' {self.apellidos}, {self.nombres}'
    def __str__(self):
        return self.nombre_completo()

class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)
    def __str__(self):
        return f'{self.nombre}, (Duración: {self.duracion} años)'

class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente_a_cargo = models.ForeignKey('Docente', null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return f'{0} - {1} - {2} años - Prof. {3}'

class Docente(Persona):
    curso_a_cargo = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    categorias = [
        ('1', 'Ayudante de Catedra'),
        ('2', 'Jefe de Trabajos Practicos'),
        ('3', 'Profesor Adjunto'),
        ('4', 'Profesor Asociado'),
        ('5', 'Titular de Catedra')
    ]
    dedicaciones = [
        ('1', 'Simple'),
        ('2', 'Semi Exclusiva'),
        ('3', 'Exclusiva')
    ]
    categoria = models.CharField(max_length=1, choices=categorias, default='1')
    dedicacion = models.CharField(max_length=1, choices=dedicaciones, default='1')
    def __str__(self):
        return f'{self.dni} - {self.nombre_completo()} - {self.curso_a_cargo} - {self.categoria} - {self.dedicacion}'

class Estudiante(Persona):
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    regularidad = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.dni} - {self.nombre_completo()} - {self.carrera} - {self.regularidad}'
