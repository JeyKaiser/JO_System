from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
]