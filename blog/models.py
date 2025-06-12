from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date
class Publicacion(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_publicacion= models.DateTimeField(default=timezone.now)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    def publicar(self):
            self.fecha_publicacion = timezone.now()
            self.save()
    def __str__(self):
            return self.titulo
class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor =  models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    categoria = models.CharField(max_length=50)
    portada = models.URLField()
    sinopsis = models.TextField()

    def __str__(self):
        return self.titulo

    def publicar(self):
        self.fecha_publicacion = date.today()
        self.save()

