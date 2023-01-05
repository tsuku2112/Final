from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo=models.CharField(max_length=40)
    subtitulo=models.CharField(max_length=40)
    publicacion=models.DateField()
    contenido=models.TextField()
    categoria=models.CharField(max_length=40)

class Autores(models.Model):
    apellido=models.CharField(max_length=40)
    nombre=models.CharField(max_length=40)
    mail=models.EmailField()
    
class Categoria(models.Model):
    nombre=models.CharField(max_length=40)
    descripcion=models.CharField(max_length=140)