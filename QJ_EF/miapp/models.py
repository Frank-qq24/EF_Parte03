from django.db import models

# Create your models here.
class producto(models.Model):
    codigo= models.TextField(max_length=10)
    nombre    = models.TextField()
    precio_compra    = models.TextField()
    precio_venta    = models.TextField()
    Fecha_compra = models.TextField()
    Fecha_registro = models.TextField()
    estado   = models.CharField(max_length=1)

class curso(models.Model):
    codigo= models.AutoField(primary_key=True)
    nombre    = models.TextField()
    horas    = models.TextField()
    creditos    = models.TextField()
    Fecha_registro = models.DateTimeField(auto_now_add=True)  
    estado   = models.CharField(max_length=1)
