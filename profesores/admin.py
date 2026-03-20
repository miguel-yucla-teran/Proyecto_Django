from django.contrib import admin
from .models import Profesor, ObservacionProfesor

# 1) Personalizar nuestro panel de administración (Branding Admin Panel)

#Cambiar los textos genéricos de Django
admin.site.site_header = "Administración Central App de Gestión Liceos"
admin.site.site_title = "Panel de Control"
admin.site.index_title = "Bienvenido al Panel de Control - App de Gestión Liceos"

# 2) Aplicar Inlines (Anotaciones)
class ObservacionProfesorAdmin(admin.StackedInline):
    model = ObservacionProfesor
    extra = 1 #Muestra una fila vacía por defecto para agregar nuevas anotaciones.

class ProfesorAdmin(admin.ModelAdmin):
    #Acá personalizamos los nombres de cada columna a mostrar del Alumno
    list_display = ("nombre", "apellido", "especialidad", "correo_electronico")

    #Podemso agregar campos de búsqueda: lupita para buscar por nombre y apellido
    search_fields = ("nombre", "apellido, especialidad")

    #Conectar el inlines (Elemento incrustado en el Modelo Registrar).
    inlines = [ObservacionProfesorAdmin]

#Registrar el Modelo Alumno (Tabla Alumno) en el panel de administración
admin.site.register(Profesor, ProfesorAdmin)
