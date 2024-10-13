from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Proyecto, Task, CustomUser
from .forms import CreateNewTask, CreateNewProject, CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import transaction


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        #print(request.POST)
        if request.POST['password1'] == request.POST['password2']:            
            try:
                with transaction.atomic(): 
                    user = CustomUser.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    email=request.POST['email']  # Agregar el email
                )
                user.save()                # Iniciar sesión automáticamente después del registro
                login(request, user)
                messages.success(request, 'Cuenta creada con éxito.')
                print('Cuenta creada con éxito.')
                return redirect('signin')  
            except Exception as e:
                print(f'Error: {e}')                
                return render(request, 'signup.html', {'miSignup': form})
        else:
            messages.error(request, 'Las contraseñas no coinciden.')
            print('Las claves no son iguales.')
            return render(request, 'signup.html', {'miSignup': form})
    else:
        form = CustomUserCreationForm(request.POST)
        return render(request, 'signup.html', {'miSignup': form})


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'miSignin': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],
                    password=request.POST['password'])
        if user is None:            
            return render(request, 'signin.html',{
            'miSignin': AuthenticationForm,
            'error': 'Usuario o Contraseña es incorrecta'
        })
        else:
            login(request, user)
            return redirect('index')
        
    
def index(request):
    title = 'Django-Course!!'
    return render(request, "index.html", {
        'mititle': title
    })
        

def proyecto(request):
    proyectos = list(Proyecto.objects.values())
    return render(request, 'proyectos/proyectos.html', {
        'miproyecto': proyectos
    })

def project_detail(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    tasks = Task.objects.filter(proyecto_id=id)
    print(proyecto)
    print(tasks)
    return render(request, 'proyectos/detail.html', {
        'detailProject': proyecto,
        'detailTask': tasks
    })


def tasks(request):
    tareas = list(Task.objects.values()) 
    return render(request, 'tareas/tasks.html', {
        'mitarea': tareas,
        
    })


def create_task(request):
    if request.method == 'GET':
        proyectos = Proyecto.objects.all()
        return render(request, 'tareas/create_task.html', {
            'miFormTask': CreateNewTask(),
            'proyectos': proyectos,
        })
        # print(request.GET)                                # Esto no genera error, solo imprime el diccionario
    else:
        print(request.POST)                             # Devuelve '' si 'titulo' no está en la solicitud
        titulo = request.POST.get('titulo', '')         # Devuelve '' si 'descripcion' no está en la solicitud
        descripcion = request.POST.get('descripcion', '')
        proyecto = Proyecto.objects.get(id=request.POST.get('proyectos'))
        Task.objects.create(
            titulo=titulo, descripcion=descripcion, proyecto=proyecto)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        # show interface
        return render(request, 'proyectos/create_project.html', {
            'miFormProject': CreateNewProject()
        })
        # print(request.GET)                                  # Esto no genera error, solo imprime el diccionario
    else:       
        nombreProject = request.POST.get('nombre', '')        # Devuelve '' si 'titulo' no está en la solicitud
        Proyecto.objects.create(nombre_proyecto = nombreProject)
        return redirect('proyecto')



def about(request):
    return render(request, "about.html")


def signout(request):
    logout(request)
    print('Salir de la sesión')
    return redirect('signin')


