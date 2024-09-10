#desde este archivo puedo añadir los modelos dentro del panel del administrador cuando ejecuto (python manage.py createsuperuser)
from django.contrib import admin
from.models import Aparrel, Proyecto, Task
# Register your models here.


#version configurable@admin.register(Aparrel)
class AparrelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'referencia',
        'fotoReferencia',
        'codigoSapMD',
        'codigoSapPT',
        'nombreSistema',
        'descripcionColor',
    )
    ordering = ('id',)
    search_fields = ('referencia',                    
                    'fotoReferencia',
                    'codigoSapMD',
                    'codigoSapPT',
                    'nombreSistema',
                    'descripcionColor',
    )

#version corta
# admin.site.register(Aparrel)

admin.site.register(Proyecto)

admin.site.register(Task)

