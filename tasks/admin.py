from django.contrib import admin
# Importar los modelos 
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("Fecha_Creacion", )

# Añadirlos al panel de admin
admin.site.register(Task, TaskAdmin) 