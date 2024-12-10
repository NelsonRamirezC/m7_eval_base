from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        ordering = ["nombre"]
        db_table = 'usuarios'

    def __str__(self):
        return self.nombre


class Fotografia(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.CharField(max_length=30)
    usuarios = models.ManyToManyField(Usuario, related_name="compartir", null=True, blank=True)

    class Meta:
        ordering = ["titulo"]
        db_table = 'fotografias'

    def __str__(self):
        return self.titulo