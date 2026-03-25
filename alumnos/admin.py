from django.contrib import admin
from .models import Alumno

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    #Acá personalizamos los nombres de cada columna a mostrar del Alumno
    list_display = ["rut", "nombre", "apellido", "fecha_nacimiento"]

    #Podemso agregar campos de búsqueda: lupita para buscar por nombre y apellido
    search_fields = ["rut", "nombre", "apellido"]

    ordering = ['apellido', 'nombre']

