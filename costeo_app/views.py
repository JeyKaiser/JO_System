from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Proyecto, Task

# Create your views here.
def index(request):
    return HttpResponse("Bienvenido al index")

def hello(request, username):    
    #print(type(username))
    print(username)
    return HttpResponse(f"<h1>Hola {username}, bienvenido</h1>")              #metodo f-string
    #return HttpResponse("<h2>Hello World %s</h2>" % username")   --metodo antiguo

def about(request):    
    return HttpResponse("<h1>Acerca de</h1>")

#muestra una lista con formato JSON, con los valores de la tabla proyectos
def proyecto(request):
    proyectos = list(Proyecto.objects.values())
    return JsonResponse(proyectos, safe=False)
    
def tasks(request, id):
    tarea = get_object_or_404(Task, id=id)
    #tarea = Tasks.objects.get(id=id)                     asi seria sin manejo de 404
    #return HttpResponse("tareas: %s" % tarea.titulo)     forma antigua
    return HttpResponse(f"Tarea con id {id}: {tarea.titulo}")