from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# TAREAS - [TABLA TAREAS]   -   MODELO 1
class Task(models.Model):
    Titulo = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    Fecha_Creacion = models.DateTimeField(auto_now_add=True)    # Fecha de creada automatica
    Fecha_Inicio = models.DateTimeField(null=True, blank=True)
    Fecha_Finalizacion = models.DateTimeField(null=True, blank=True)
    Importante = models.BooleanField(default=False)

    # Para relacionarla con algo de un usuario
    # Relacion de tabla tareas con el usuario correspondiente que la creo
    # Cuando se elimine El usuario. Eliminar lo que creo
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Mostrar Titulo de la tarea y el creador
    def __str__(self):
        return self.Titulo + ' - Created by:  ' + self.user.username

# 