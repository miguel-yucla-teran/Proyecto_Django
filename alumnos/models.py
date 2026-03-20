from django.db import models

#Acá las clases creadas se usarán para construir la BD:
# - 1)Se crearán clases python acá.
# - 2)Se leerán y creará un plano para 'migrarlas' a las BD como tablas ORM
# - 3)Una vez listo el plano (migración), se ejecuta la migración en la BD
# - 4)Se creó la tabla espejo de cada clase python escrita acá.
#       *Si existe la Clase Alumno acá.
#        *Existe la tabla Alumno en la BD
# - 5)Estas tablas podrán ser utilizadas por el módulo de administración nativa en Django o tu Front-End.

#Un MODEL de Django = Clase Python
#Una vez que lee esta clase es como si ejecutaramos un CREATE TABLE Alumno(...);

class Alumno(models.Model):

    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    correo_electronico = models.EmailField(unique=True, verbose_name="Email")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Anotacion(models.Model):
    #Acá se crea una FK que apunta automaticamente a la PK de la otra tabla modelo.

    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    anotacion = models.TextField(verbose_name="Anotacion")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha")

    def __str__(self):
        return f"Anotación de {self.alumno} el {self.fecha}"