from django import forms

class ProfesorForm(forms.Form):
    #Si es del tipo texto, debe ser Charfield
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    especialidad = forms.CharField(label='Especialidad', max_length=100)
    #Si es del tipo EMAIL, automaticamente va a validar que tenga @ y un formato final de .cl
    correo_electronico = forms.EmailField(label='Correo Electrónico')