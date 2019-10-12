from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date, datetime

# Create your models here.

class Comunidad(models.Model):
    id = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=200)
    municipio = models.CharField(max_length=200)
    comunidad = models.CharField(max_length=200)

    def __str__(self):
        return self.comunidad

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s' % (self.nombre, self.apellido)

    class Meta:
        ordering = ['nombre']

class Actividad(models.Model):
    id = models.AutoField(primary_key=True)
    nombreActividad = models.CharField(max_length=200)
    fecha = models.DateField(null=True, blank=True)
    hora = models.TimeField(null=True, blank=True)
    lugar = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    conferencista = models.CharField(max_length=200)
    
    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Persona(update etc)
        """
        return reverse('aplicacion:actividad-detail', args=[str(self.id)])

    def __str__(self):
        return self.nombreActividad

class Participante_Actividad(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.SET_NULL, null=True)
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, verbose_name='Participantes')