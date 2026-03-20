from django.db import models

class Profesor(models.Model):

    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    especialidad = models.CharField(max_length=100, verbose_name="Especialidad")
    correo_electronico = models.EmailField(unique=True, verbose_name="Email")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class ObservacionProfesor(models.Model):
    #Acá se crea una FK que apunta automaticamente a la PK de la otra tabla modelo.

    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    observacion = models.TextField(verbose_name="Observacion")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha")

    def __str__(self):
        return f"Observación de {self.profesor} el {self.fecha}"