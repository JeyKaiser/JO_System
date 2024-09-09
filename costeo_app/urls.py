from django.urls import path, include
from . import views

#coments
urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('proyecto', views.proyecto),
    path('tasks/<int:id>', views.tasks),
]

