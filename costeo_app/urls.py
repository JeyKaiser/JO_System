from django.urls import path, include
from . import views


#COMENTARIO DE PUEBA PARA CREAR UN COMMIT
urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
]