from django.http import HttpResponse
from django.shortcuts import render
from techrealm.models import *
from techrealm.forms import *

def blogs(request):
    if request.method == 'POST':
        blog = Blogs(nombre = request.POST.get('nombreBlog'), tema = request.POST.get('temaBlog'))
        blog.save()
    return render(request, 'blogs.html')

def cursos(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid:
            curso = Cursos(nombre = request.POST.get('nombreCurso'), nivel = request.POST.get('nivelCurso'), fecha = request.POST.get('fechaCurso'))
            curso.save()
    return render(request, 'cursos.html')
    
def inicio(request):
    flagBusqueda = False
    if request.method == 'POST':
        nombreCurso = request.POST.get('nombreCurso')
        cursos = Cursos.objects.filter(nombre__icontains = nombreCurso)
        flagBusqueda = True
    else:
        cursos = Cursos.objects.all()
    contexto = {"flag": flagBusqueda,"cursos": cursos}
    return render(request, 'inicio.html', contexto)

def libros(request):
    if request.method == 'POST':
        libro = Libros(nombre = request.POST.get('nombreLibro'), tema = request.POST.get('temaLibro'), codigo = request.POST.get('codigoLibro'))
        libro.save()
    return render(request, 'libros.html')