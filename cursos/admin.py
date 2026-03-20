from django.contrib import admin
from .models import Curso, NovedadCurso

# 1) Personalizar nuestro panel de administración (Branding Admin Panel)

#Cambiar los textos genéricos de Django
admin.site.site_header = "Administración Central App de Gestión Liceos"
admin.site.site_title = "Panel de Control"
admin.site.index_title = "Bienvenido al Panel de Control - App de Gestión Liceos"
class NovedadCursoAdmin(admin.StackedInline):
    model = NovedadCurso
    extra = 1 #Muestra una fila vacía por defecto para agregar nuevas anotaciones.

class CursoAdmin(admin.ModelAdmin):
    #Acá personalizamos los nombres de cada columna a mostrar del Alumno
    list_display = ("nombre", "descripcion")

    #Podemso agregar campos de búsqueda: lupita para buscar por nombre y apellido
    search_fields = ("nombre", "descripcion")

    #Conectar el inlines (Elemento incrustado en el Modelo Registrar).
    inlines =[NovedadCursoAdmin]

#Registrar el Modelo Alumno (Tabla Alumno) en el panel de administración
admin.site.register(Curso, CursoAdmin)

