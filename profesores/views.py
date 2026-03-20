from django.shortcuts import render
from .import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def portal_profesores(request):
    return render(request, "profesores/profesores.html")

@login_required
def lista_profesores(request):
    profesores = ["Profesor Rosa", "Profesor Jirafales", "Profesor Ramon", "Profesor Longaniza"]
    contexto = {'lista_profesores': profesores
                }
    return render(request, "profesores/lista_profesores.html", contexto)

@login_required
def nuevo_profesor(request):
    if request.method == 'GET':
        #Acá llegaria cuando la persona apretó el boton de la barra de navegación, buscando el link
        form = forms.ProfesorForm()
    else:
        #Acá llegaría cuando la persona apretó el boton del formulario 'Crear Alumno'
        form = forms.ProfesorForm(request.POST)
        if form.is_valid():
            #Acá extraemos los datos de la solicitud Http (request) y los asignamos variables
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            especialidad = form.cleaned_data['especialidad']
            correo_electronico = form.cleaned_data['correo_electronico']
            contexto_post = {'nombre': nombre,
                             'apellido': apellido,
                             'especialidad': especialidad,
                             'correo_electronico': correo_electronico,
                             }


            #Acá yo debería tomar las variables y guardarlas en MySql(persistir los datos)

            #Debería enviar un mensaje de confirmación "Nuevo alumno creado con éxito"
            return render(request, "profesores/registro_exito.html", contexto_post)

    contexto = {
                'form': form
                }

    return render(request, "profesores/registro_profesor.html", contexto)
