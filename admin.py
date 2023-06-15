from django.contrib import admin
from .models import Registro


admin.site.register(Registro)

class RegistroAdmin(admin.ModelAdmin):
    list_display = ('expediente', 'unidad_fiscalizable', 'nombre_razon_social', 'categoria', 'region', 'estado', 'detalle')


admin.site.register(Registro, RegistroAdmin)
