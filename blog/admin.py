from django.contrib import admin
from .models import Publicacion
from .models import Libro
admin.site.register(Publicacion)
admin.site.register(Libro)