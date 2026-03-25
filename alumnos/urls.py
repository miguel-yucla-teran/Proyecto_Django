from django.urls import path
from .import views

urlpatterns = [
    path("home/", views.inicio, name="portal_alumnos"),

    path("lista/", views.lista_alumnos, name="lista_alumnos"),

    path("agregar/", views.agregar_alumno, name="agregar_alumno"),

    path('<str:rut>/detalle/', views.detalle_alumno, name='detalle_alumno'),
    path('<str:rut>/editar/', views.editar_alumno, name='editar_alumno'),
    path('<str:rut>/eliminar/', views.eliminar_alumno, name='eliminar_alumno'),
]