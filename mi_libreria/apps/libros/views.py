from django.shortcuts import render
from .models import Libro

def lista_libros(request):
    libros = Libro.objects.select_related('autor').all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})

