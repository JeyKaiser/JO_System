from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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
    

class Telas(models.Model):
    id = models.AutoField(primary_key=True)
    cod_tela = models.CharField(max_length=30, null=True, blank=True)
    descripcion_tela = models.CharField(max_length=30, null=True, blank=True)
    ancho = models.CharField(max_length=50, null=True, blank=True)
    cod_color = models.CharField(max_length=30, null=True, blank=True)
    descripcion_color = models.CharField(max_length=30, null=True, blank=True)
    

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # Agrega este campo

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  # Campos obligatorios además de USERNAME_FIELD

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    
