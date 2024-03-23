from django.contrib import admin
from .models import Carrera, Estudiante, Curso

class CarreraAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nombre", "duracion"]

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ["dni", "apellidos", "nombres", "fecha_nacimiento", "genero", "carrera", "regularidad"]

class CursoAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nombre", "creditos", "docente_a_cargo"]

# crear modelo DOCENTE, que DOCENTE y Estudiante hereden
# o de un modelo Persona
# o del modelo Users que ya me provee django, donde creé el superuser

# Register your models here.
admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Curso, CursoAdmin)