from django.contrib import admin
from .models import Carrera, Estudiante, Curso, Docente

class CarreraAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nombre", "duracion"]

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ["dni", "apellidos", "nombres", "fecha_nacimiento", "genero", "carrera", "regularidad"]

class DocenteAdmin(admin.ModelAdmin):
    list_display = ["dni", "apellidos", "nombres", "fecha_nacimiento", "genero", "curso_a_cargo", "categoria", "dedicacion" ]


class CursoAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nombre", "creditos", "docente_a_cargo"]

admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Docente, DocenteAdmin)