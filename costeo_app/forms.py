from django import forms
    
class CreateNewTask(forms.Form):
    titulo = forms.CharField(label="Nombre de tarea", max_length=200)
    descripcion = forms.CharField(label="Descripcion de la tarea", widget=forms.Textarea)

class CreateNewProject(forms.Form):
    nombre = forms.CharField(label="Nombre del proyecto", max_length=200)
