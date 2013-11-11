from django.db import models

# Create your models here.

class Alumno(models.Model):
        nombre = models.CharField(max_length=50)
        edad = models.IntegerField()
        carrera = models.CharField(max_length=4)

class ass(models.Model):
        aaa = models.CharField(max_length=10)
