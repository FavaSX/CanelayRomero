from django.db import models

# Create your models here.
class Torta(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.TextField()
    precio=models.IntegerField()
    def __str__(self):
        return self.nombre
    
class coctel(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.TextField()
    precio=models.IntegerField()
    def __str__(self):
        return self.nombre
    
class pan_pascua(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.TextField()
    precio=models.IntegerField()
    def __str__(self):
        return self.nombre
