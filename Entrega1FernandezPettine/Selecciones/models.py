from django.db import models
from pyexpat import model


# Create your models here.
class Selecciones(models.Model): #Se crea la clase de selecciones de futbol

    name = models.CharField(max_length=30) # Se crea el modelo name, que contiene el nombre de la selección
    continent = models.CharField(max_length=20) # Se crea el modelo continent, que alberga el continente del país
    ranking = models.FloatField(max_length=5) # Se crea el modelo ranking, que contiene la clasificacion en el ranking mundial

