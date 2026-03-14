from django import forms

class CursoForm(forms.Form):
    #Si es del tipo texto, debe ser Charfield
    nombre_curso = forms.CharField(label='Nombre_curso', max_length=100)
    codigo = forms.CharField(label='Codigo', max_length=100)
    descripcion = forms.CharField(label='Descripcion', widget=forms.Textarea,required=False  )
    profesor = forms.CharField(label='Profesor', max_length=100)
