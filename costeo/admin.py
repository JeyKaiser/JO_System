from django.contrib import admin
from.models import Aparrel
# Register your models here.

#version corta
# admin.site.register(Aparrel)

#version configurable
@admin.register(Aparrel)
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
    search_fields = (
        'referencia',
        'fotoReferencia',
        'codigoSapMD',
        'codigoSapPT',
        'nombreSistema',
        'descripcionColor'
    )