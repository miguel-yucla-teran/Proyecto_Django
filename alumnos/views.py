from django.shortcuts import render
from .import forms


# Create your views here.
def portal_alumnos(request):
    return render(request, "alumnos/inicio.html")

def lista_alumnos(request):
    alumnos = ["Chuck Norris", "Bruce Lee", "Jet Li", "Jackie Chan"]
    contexto = {'lista_alumnos': alumnos
                }
    return render(request, "alumnos/lista_alumnos.html", contexto)

def nuevo_alumno(request):
    if request.method == 'GET':
        #Acá llegaria cuando la persona apretó el boton de la barra de navegación, buscando el link
        form = forms.AlumnoForm()
    else:
        #Acá llegaría cuando la persona apretó el boton del formulario 'Crear Alumno'
        form = forms.AlumnoForm(request.POST)
        if form.is_valid():
            #Acá extraemos los datos de la solicitud Http (request) y los asignamos variables
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            correo_electronico = form.cleaned_data['correo_electronico']
            contexto_post = {'nombre': nombre,
                             'apellido': apellido,
                             'correo_electronico': correo_electronico,
                             }


            #Acá yo debería tomar las variables y guardarlas en MySql(persistir los datos)

            #Debería enviar un mensaje de confirmación "Nuevo alumno creado con éxito"
            return render(request, "alumnos/registro_exito.html", contexto_post)

    contexto = {
                'form': form
                }

    return render(request, "alumnos/registro_alumno.html", contexto)