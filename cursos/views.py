from django.shortcuts import render
from .import forms

# Create your views here.
def portal_cursos(request):
    return render(request, "cursos/cursos.html")

def lista_cursos(request):
    cursos = ["1A", "1B", "1C", "1D"]
    contexto = {'lista_cursos': cursos
                }
    return render(request, "cursos/lista_cursos.html", contexto)

def nuevo_curso(request):
    if request.method == 'GET':
        #Acá llegaria cuando la persona apretó el boton de la barra de navegación, buscando el link
        form = forms.CursoForm()
    else:
        #Acá llegaría cuando la persona apretó el boton del formulario 'Crear Alumno'
        form = forms.CursoForm(request.POST)
        if form.is_valid():
            #Acá extraemos los datos de la solicitud Http (request) y los asignamos variables
            nombre_curso = form.cleaned_data['nombre_curso']
            codigo = form.cleaned_data['codigo']
            descripcion = form.cleaned_data['descripcion']
            profesor = form.cleaned_data['profesor']

            contexto_post = {'nombre_curso': nombre_curso,
                             'codigo': codigo,
                             'descripcion': descripcion,
                             'profesor': profesor,
                             }


            #Acá yo debería tomar las variables y guardarlas en MySql(persistir los datos)

            #Debería enviar un mensaje de confirmación "Nuevo alumno creado con éxito"
            return render(request, "cursos/registro_exito.html", contexto_post)

    contexto = {
                'form': form
                }

    return render(request, "cursos/registro_curso.html", contexto)

