from django.urls import path
from .import views

urlpatterns = [
    path("home/", views.portal_cursos, name="inicio_cursos"),
    ]
