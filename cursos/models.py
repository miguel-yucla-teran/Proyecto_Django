from django.db import models

class Curso(models.Model):

    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class NovedadCurso(models.Model):
    #Acá se crea una FK que apunta automaticamente a la PK de la otra tabla modelo.

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    detalle = models.TextField(verbose_name="Detalle")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha")

    def __str__(self):
        return f"Anotación de {self.curso} el {self.detalle}"