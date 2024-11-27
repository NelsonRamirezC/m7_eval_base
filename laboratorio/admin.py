from django.contrib import admin

from .models import Laboratorio, Producto, DirectorGeneral

# Register your models here.


admin.site.register(Laboratorio)
admin.site.register(Producto)
admin.site.register(DirectorGeneral)
