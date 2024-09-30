from django.urls import path, include
from . import views

#coments
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('proyecto/', views.proyecto, name='proyecto'),
    path('tasks/', views.tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_project'),
    path('hello/<str:username>', views.hello, name='hello'),
    #path('tasks/<int:id>', views.tasks),
]

