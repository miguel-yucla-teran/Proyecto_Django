from django.contrib import admin
from .models import Alumno, Anotacion

# 1) Personalizar nuestro panel de administración (Branding Admin Panel)

#Cambiar los textos genéricos de Django
admin.site.site_header = "Administración Central App de Gestión Liceos"
admin.site.site_title = "Panel de Control"
admin.site.index_title = "Bienvenido al Panel de Control - App de Gestión Liceos"

# 2) Aplicar Inlines (Anotaciones)
class AnotacionAdmin(admin.StackedInline):
    model = Anotacion
    extra = 1 #Muestra una fila vacía por defecto para agregar nuevas anotaciones.

class AlumnoAdmin(admin.ModelAdmin):
    #Acá personalizamos los nombres de cada columna a mostrar del Alumno
    list_display = ("nombre", "apellido", "correo_electronico")

    #Podemso agregar campos de búsqueda: lupita para buscar por nombre y apellido
    search_fields = ("nombre", "apellido")

    #Conectar el inlines (Elemento incrustado en el Modelo Registrar).
    inlines = [AnotacionAdmin]

#Registrar el Modelo Alumno (Tabla Alumno) en el panel de administración
admin.site.register(Alumno, AlumnoAdmin)
