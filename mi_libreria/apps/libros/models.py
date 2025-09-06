from django.db import models
from apps.autores.models import Autor

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField(null=True, blank=True)
    paginas = models.IntegerField(null=True, blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
