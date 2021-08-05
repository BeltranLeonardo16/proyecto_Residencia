from django.db import models

# Create your models here.

class Perfil(models.Model):
    id_Perfil = models.AutoField(primary_key = True)
    contrasena = models.CharField(max_length = 100)
    correo = models.EmailField(max_length = 100)

class Usuario(models.Model):
    id_Usuario = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    correo = models.EmailField(max_length = 100)
    edad = models.IntegerField()
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

class Calificacion(models.Model):
    id_Calificacion = models.AutoField(primary_key = True)
    calif_Unidad = models.FloatField()

class Evaluacion(models.Model):
    id_Evaluacion = models.AutoField(primary_key = True)
    no_Evaluacion = models.IntegerField()
    nombre_Evaluacion = models.CharField(max_length = 20)
    no_Aciertos = models.IntegerField()
    respuestas_correctas = models.IntegerField()
    calificacion = models.ForeignKey(Calificacion, on_delete=models.CASCADE)


