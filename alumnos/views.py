from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from alumnos.models import Alumno
from alumnos.forms import AlumnoForm
from django.contrib import messages

@login_required()
def inicio(request):
    return render(request, "alumnos/inicio.html")

@login_required
def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    contexto = {'lista_alumnos': alumnos
                }
    return render(request, "alumnos/lista_alumnos.html", contexto)
@login_required
def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno =form.save()
            messages.success(request, f"El alumno {alumno.nombre} {alumno.apellido} fue registrado con exito")
            return redirect('lista_alumnos')
    else:

        form = AlumnoForm()
    contexto = {'form': form}
    return render(request, "alumnos/agregar_alumno.html", contexto)

@login_required
def detalle_alumno(request, rut):
    alumno = get_object_or_404(Alumno, rut=rut)
    contexto = {'alumno':alumno}
    return render(request, 'alumnos/detalle_alumno.html', contexto)

@login_required
def editar_alumno(request, rut):
    alumno = get_object_or_404(Alumno, rut=rut)
    if request.method == 'POST':
        # Acá estoy programando lo que pasa cuando la persona pinchó en el botón EDITAR ALUMNO (POST)
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            # Acá ejecuto el UPDATE en la BD
            alumno = form.save()
            messages.success(
                request,
                f'El alumno {alumno.nombre} {alumno.apellido} fue actualizado con éxito.'
            )
            return redirect('lista_alumnos')
    else:
        # Acá estoy programando lo que pasa cuando la persona pinchó en el ICONO LÁPIZ (GET)
        form = AlumnoForm(instance=alumno)
    contexto = {'form': form, 'alumno': alumno}
    return render(request, 'alumnos/editar_alumno.html', contexto)

@login_required
def eliminar_alumno(request, rut):
    alumno = get_object_or_404(Alumno, rut=rut)
    if request.method == 'POST':
        alumno.delete()
        messages.success(
            request,
            f'El alumno {alumno.nombre} {alumno.apellido} fue eliminado del sistema.'
        )
        return redirect('lista_alumnos')
    contexto = {'alumno':alumno}
    return render(request, 'alumnos/eliminar_alumno.html', contexto)