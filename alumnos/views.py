from django.shortcuts import render


# Create your views here.
def portal_alumnos(request):
    return render(request, "alumnos/inicio.html")

def lista_alumnos(request):
    alumnos = ["Chuck Norris", "Bruce Lee", "Jet Li", "Jackie Chan"]
    contexto = {'lista_alumnos': alumnos
                }
    return render(request, "alumnos/lista_alumnos.html", contexto)