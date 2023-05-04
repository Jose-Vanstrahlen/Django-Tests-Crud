
from django.forms import ModelForm      #FORMULARIO
from .models import Task                #MODELO 1 - Modelo de Tarea
from django import forms



# FORMULARIO PARA CREAR TAREAS
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields  = ['Titulo','description','Importante']
        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo de la tarea'}),

            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe la tarea'}),

            'Importante': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
# --------------------------------------------------------
