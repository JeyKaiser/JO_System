from django.db import models

# Create your models here.

class Aparrel(models.Model):
    id = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=30, null=True, blank=True)
    fotoReferencia = models.CharField(max_length=30, null=True, blank=True)
    codigoSapMD = models.CharField(max_length=30, null=True, blank=True)
    codigoSapPT = models.CharField(max_length=30, null=True, blank=True)
    nombreSistema = models.CharField(max_length=30, null=True, blank=True)
    descripcionColor = models.CharField(max_length=30, null=True, blank=True)

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=50)

    #(metodo) funcion que permite extender, mostrar algo en la interfaz superuser
    def __str__(self):
        return self.nombre_proyecto

class Task(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)    
    done = models.BooleanField(default=False) 
    
    def __str__(self):
        return self.titulo
    
    