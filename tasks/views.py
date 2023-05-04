from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# ------ Importar Modelos/Clases ------

from django.contrib.auth.models import User              #--- Para Registrar Ususaios (Django)
from django.contrib.auth.forms import UserCreationForm   #--- Clase Para Formulario SINGUP [Crear Usuario]
from django.contrib.auth.forms import AuthenticationForm #--- Clase Para Formulario SINGIN [Login]
from django.contrib.auth import login, logout, authenticate #--- 

from .forms import TaskForm                             #--- Formulario Tarea

from .models import Task                                #--- Modelo 1 - Modelo de Tareas

from django.shortcuts import get_object_or_404          #--- Para devolver Error 404 en caso de no existir algo
from django.db import IntegrityError                    #--- Para manejar error de integridad

from django.utils import timezone

from django.contrib.auth.decorators import login_required

from django.urls import reverse




def home(request):
    return render(request, 'home.html')


# --------------------------------------------------------
# Funcion Singup - [Crear Usuario]
def singup(request):
    if request.method == 'GET':
        return render(request, 'singup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Registrar Usuario
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                # Guardarlo en La BD
                user.save()
                # 
                login(request, user)
                # Despues de crear el usuario, redireccionar
                return redirect('tasks')
            except IntegrityError:
                # En caso de que el user ya exista
                return render(request, 'singup.html', {
                    'form': UserCreationForm,
                    'error': 'El Usuario Ya existe'
                })
        else:
            # Si las contraseñas no coinciden
            return render(request, 'singup.html', {
                'form': UserCreationForm,
                "error": 'Contraseñas No Coinciden'
            })
        

# --------------------------------------------------------
# Funcion Tareas - [Ver/Lisar Tareas]
@login_required
def tasks (request):
    tasks = Task.objects.filter(user=request.user, Fecha_Finalizacion__isnull=True) # Fecha_Finalizacion__isnull=True
    return render(request, 'tasks.html',{'tasks': tasks})

@login_required
# Funcion Crear Tareas
def create_tasks (request):
    if request.method == 'GET':
        return render(request, 'create_tasks.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_tasks.html', {
                'form': TaskForm,
                'error': 'Datos Invalidos',
            })

@login_required    
# Funcion Detalles Tarea - Actualizar
def tasks_detail (request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)      #-- Actualizar Tarea
        return render(request, 'tasks_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'tasks_detail.html', {'task': task, 'form': form, 'error': "Error al Intentar Actualizar"})

@login_required
# Funcion Completar Tarea
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.Fecha_Finalizacion = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
# Funcion Eliminar Tarea
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')

@login_required
# Funcion Mostrar Tareas Completadas
def complete_list_task(request):
    tasks = Task.objects.filter(user=request.user, Fecha_Finalizacion__isnull=False).order_by('-Fecha_Finalizacion')
    return render(request, 'complete_list_task.html',{'tasks': tasks})


# --------------------------------------------------------
@login_required
# Funcion Logout - [Cerrar Sesion]
def cerrar_sesion (request):
    logout(request)
    return redirect('home')


# --------------------------------------------------------
# Funcion Singin - [Iniciar Cesion]
def singin(request):
    if request.method == 'GET':
        return render(request, 'singin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        # En caso de error, o no existir
        if user is None:
            return render(request, 'singin.html', {
            'form': AuthenticationForm,
            'error': 'Nombre de Usuario o Contraseña Incorrecto'
            })
        # En caso de si existir, se redirecciona
        else:
            #Guardarle su sesion
            login(request, user)
            return redirect ('tasks')
# --------------------------------------------------------

