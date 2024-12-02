from django.contrib import admin

from .models import Laboratorio, Producto, DirectorGeneral

# Register your models here.

class LaboratorioAdmin(admin.ModelAdmin):
    fields = ["nombre"]
    list_display = ["id", "nombre"]
    list_display_links = ["nombre"]
    search_fields = ["nombre"]
    ordering = ["id"]
    list_filter = ["nombre"]
    
    
class ProductoAdmin(admin.ModelAdmin):
    fields = ["nombre"]
    list_display = ["id", "nombre", "laboratorio", "f_fabricacion", "precio_costo", "precio_venta"]
    list_display_links = ["nombre", "laboratorio"]
    search_fields = ["nombre"]
    ordering = ["id"]
    list_filter = ["laboratorio"]
    

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(DirectorGeneral)
