from django.db import models

class Vehiculo(models.Model):
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    anio = models.CharField(max_length=200)
    tipo_vehiculo = models.CharField(max_length=200)
    nombre_corto = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_corto
