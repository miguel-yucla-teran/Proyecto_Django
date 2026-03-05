from django.shortcuts import render

# Create your views here.
def portal_profesores(request):
    return render(request, "profesores/profesores.html")


