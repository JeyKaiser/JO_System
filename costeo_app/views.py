from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Proyecto, Task, CustomUser
from .forms import CreateNewTask, CreateNewProject
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    title = 'Django-Course!!'
    return render(request, "index.html",{
        'mititle': title
    })

def about(request):
    return render(request, "about.html")

#muestra una lista con formato JSON, con los valores de la tabla proyectos
def proyecto(request):
    proyectos = list(Proyecto.objects.values())
    return render(request, 'proyectos/proyectos.html',{
        'miproyecto': proyectos
    })
    
def tasks(request):
    tareas = list(Task.objects.values())
    return render(request, 'tareas/tasks.html',{
        'mitarea': tareas
    })
    
def create_task(request):
    if request.method == 'GET':
        #show interface
        return render(request, 'tareas/create_task.html', {
        'miFormTask': CreateNewTask()
        })
        #print(request.GET)                                # Esto no genera error, solo imprime el diccionario        
    else:
        titulo = request.POST.get('titulo', '')            # Devuelve '' si 'titulo' no está en la solicitud
        descripcion = request.POST.get('descripcion', '')  # Devuelve '' si 'descripcion' no está en la solicitud
        Task.objects.create(titulo=titulo, descripcion= descripcion, proyecto_id=2)
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        #show interface
        return render(request, 'proyectos/create_project.html', {
        'miFormProject': CreateNewProject()
        })
        #print(request.GET)                                # Esto no genera error, solo imprime el diccionario        
    else:
        nombreProject = request.POST.get('nombre', '')            # Devuelve '' si 'titulo' no está en la solicitud
        Proyecto.objects.create(nombre_proyecto= nombreProject)
        return redirect('proyecto')
    
def project_detail(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    tasks =Task.objects.filter(proyecto_id=id)
    print(proyecto)
    print(tasks)
    return render(request, 'proyectos/detail.html', {
        'detailProject': proyecto,
        'detailTask': tasks
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = CustomUser.objects.create_user(username= request.POST['username'],
                                                password= request.POST['password1'])
                user.save()
                login(request, user)  # Iniciar sesión automáticamente después del registro
                messages.success(request, 'Cuenta creada con éxito.')
                return redirect('index')  # Redirigir a la página de inicio
            except:
                messages.error(request, 'Error en la creación de la cuenta.')
        else:
            messages.error(request, 'Error en la creación de la cuenta.')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'miSignup': form})

##def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente después del registro
            messages.success(request, 'Cuenta creada con éxito.')
            return redirect('index')  # Redirigir a la página de inicio
        else:
            messages.error(request, 'Error en la creación de la cuenta.')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'miSignup': form})


    #tarea = get_object_or_404(Task, id=i)
    #tarea = Tasks.objects.get(id=id)                     asi seria sin manejo de 404
    #return HttpResponse("tareas: %s" % tarea.titulo)     forma antigua
    #return HttpResponse(f"Tarea con id {id}: {tarea.titulo}")

def hello(request, username):    
    #print(type(username))
    print(username)
    return HttpResponse(f"<h1>Hola {username}, bienvenido</h1>")              #metodo f-string
    #return HttpResponse("<h2>Hello World %s</h2>" % username")   --metodo antiguo
