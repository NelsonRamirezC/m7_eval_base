import datetime
from django.db import models

# Create your models here.
class DirectorGeneral(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
   
    def __str__(self):
        return self.nombre
    
    def nombre_mayusculas(self):
        return self.nombre.upper()
 
    class Meta:
        managed = True
        db_table = 'directores_generales'


class Laboratorio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    director = models.OneToOneField(DirectorGeneral, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Laboratorio: {self.nombre}, Director: {self.director.nombre}"

    class Meta:
        managed = True
        db_table = 'laboratorios'



def anio_actual():
        return int(datetime.date.today().year)
 
class Producto(models.Model):
    anios_choices = [
        (anio, str(anio)) for anio in range(2015, anio_actual()+1)
    ]
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name='Producto')
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.SET_NULL, blank=True, null=True)
    f_fabricacion = models.IntegerField(choices=anios_choices, default=anio_actual(), verbose_name='F Fabricación')
    precio_costo =  models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    precio_venta =  models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=9999999)
    
    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'productos'
        