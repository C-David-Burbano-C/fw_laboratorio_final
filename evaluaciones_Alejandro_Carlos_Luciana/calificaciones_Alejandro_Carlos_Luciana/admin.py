from django.contrib import admin
from .models import Calificacion

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre_estudiante', 'identificacion', 'asignatura', 'promedio')
    search_fields = ('nombre_estudiante', 'identificacion', 'asignatura')
    readonly_fields = ('promedio',)
