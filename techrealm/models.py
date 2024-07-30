from django.db import models

class Cursos(models.Model):
    nombre = models.CharField(max_length=100)
    
    niveles = {
        "1": "Básico",
        "2": "Intermedio",
        "3": "Avanzado"
    }
    nivel = models.CharField(
        max_length = 1,
        choices = niveles,
        default = "1"
    )

    fecha = models.DateField()

class Blogs(models.Model):
    nombre = models.CharField(max_length=100)
    
    temas = {
        "1":"GTM",
        "2":"GA4",
        "3":"BQ"
    }
    tema = models.CharField(
        max_length = 1,
        choices = temas,
        default = "1"
    )

class Libros(models.Model):
    nombre = models.CharField(max_length=100)

    temas = {
        "1":"GTM",
        "2":"GA4",
        "3":"BQ"
    }
    tema = models.CharField(
        max_length= 1,
        choices = temas,
        default = "1"
    )

    codigo = models.CharField(max_length=30)
