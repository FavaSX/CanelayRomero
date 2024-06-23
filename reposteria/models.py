from django.db import models

# Create your models here.
class Torta(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.TextField()
    precio=models.IntegerField()
    imagen=models.ImageField(upload_to="tortas", null=True)
    def __str__(self):
        return self.nombre

    
class Coctel(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.TextField()
    precio=models.IntegerField()
    imagen=models.ImageField(upload_to="coctels", null=True)
    def __str__(self):
        return self.nombre
    
class Pan_pascua(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.TextField()
    precio=models.IntegerField()
    imagen=models.ImageField(upload_to="pan_pascuas", null=True)
    def __str__(self):
        return self.nombre
    
opciones_consultas = [
    [0, "Reposteria"],
    [1, "Eventos"],
    [2, "Pan de Pascua"],
]    
 
class Contacto(models.Model):
    nombre=models.CharField(max_length=15)
    apellido=models.CharField(max_length=15)
    telefono=models.IntegerField()
    correo=models.EmailField()
    tipo=models.IntegerField(choices=opciones_consultas)
    mensaje= models.TextField()
    def __str__(self):
        return self.nombre
