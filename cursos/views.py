from django.shortcuts import render

# Create your views here.
def portal_cursos(request):
    return render(request, "cursos/cursos.html")



