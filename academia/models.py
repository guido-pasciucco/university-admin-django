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
    # convertir en docenteS a cargo, y que haya un cupo para cada profe x categoría (solo1 titular, hasta 3 ayudantes, etc.)
    docente_a_cargo = models.ForeignKey('Docente', null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.codigo} - {self.nombre} - {self.creditos} años - Prof. {self.docente_a_cargo}'

class Docente(Persona):
    curso_a_cargo = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    # no puede ser docente de 2 categorías diferentes en el mismo curso
    categorias = [
        ('1', 'Ayudante de Catedra'),
        ('2', 'Jefe de Trabajos Practicos'),
        ('3', 'Profesor Adjunto'),
        ('4', 'Profesor Asociado'),
        ('5', 'Titular de Catedra')
    ]
    # dedicación simple (hasta 4 puestos docentes) - semi-exclusiva (2) - exclusiva (1)
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


# class matricula_docente(models.Model):

# class matricula_estudiante(models.Model):
"""
idea, crear un matricula_docente que cree la relación entre los docentes y un curso (una materia / cátedra)
entonces la asociación no aparece cuando se crea uno o el otro, trayendo problemas de recursividad
sino que se crean por separado y luego se asignan allí, modificandolos luego, no permitiendo la creación 
en el acto de un curso o un docente

Es decir, vos abris el panel de un curso y arrancan libres los espacios
Titular de Cátedra : vacío - hasta 1 persona
Profesor Asociado : vacío - hasta 2 personas
Profesor Adjunto : vacío - hasta 2 personas
Jefe de Trabajos prácticos - vacío - hasta 4 personas
Ayudante de cátedra : vacío - hast 4 personas
y en cada uno aparece un menú desplegable con todos los profesores disponibles, que vos lo vás estableciendo
a través de la matrícula_docente 

---

por otro lado está matrícula_estudiante, que es donde se hace la asociación del estudiante con el curso en el que está inscripto
la idea es que puedan ser varios cursos (como cuando uno en la facultad, en un cuatrimestre, se anota a varias materias)
nota: el estudiante primero se tiene que anotar a una CARRERA - la carrera está compuesta de varias MATERIAS
ordenadas en un PLAN DE ESTUDIO
primero debe estar inscripto en la carrera para luego poder inscribirse en las materias
además de que debe cumplir con LAS CORRELATIVIDADES
al mismo tiempo, cada materia va a tener diferentes CÁTEDRAS, que se van a organizar en diferentes COMISIONES (TM, TT, TN)
cada una tendrá un día y horario de cursada, crear el sistema de anotación a las materias de forma que el estudiante
no pueda inscribirse a materias que se chocan de horarios, solo se pueda inscribir a 1 comisión por materia (un turno en este caso)
y solo a 1 cátedra


MODIFICACIONES AL MODELO CURSO (materia)
- Establecer asociación con una carrera - "esta matería pertenece a esta carrera"
- Establecer régimen de correlatividades - "el estudiante puede cursar esta materia si ya rindió otras materias"
- Establecerles lugar en el plan de estudio de la carrera asociada - campo carrera y cuatrimestre debería ser suficiente
- Establecerles distintas cátedras - cada una con un nombre y un equipo docente
- cada cátedra tendrá sus horarios - (TM, TT, TN) - ejemplos:
    - TM - Lunes de 10 a 12
    - TM - Jueves de 10 a 12
    - TT - Miercoles de 15 a 17
    - TN - Martes de 18 a 21
    - TN - Jueves de 18 a 21
    - TN - Viernes de 18 a 21

MODIFICACIONES AL MODELO ESTUDIANTE
Cada estudiante va a tener:
- una carrera en la que está inscripto
- una lista de las materias en las que es anotó
- una lista de materias_aprobadas - que es necesario para calcular las correlatividades
"""


