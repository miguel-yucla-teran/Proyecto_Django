from django.urls import path
from .import views

urlpatterns = [
    path("home/", views.portal_profesores, name="inicio_profesores"),
    ]
