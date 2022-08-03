from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse

# Create your views here.
def integrantes(request):
    integrantes = ['Julca Espillco Humberto','Quintana Quispe Frank']
    return render(request, 'integrantes.html', {
        'titulo':'Integrantes del proyecto',
        'integrantes':integrantes
    })

def saludo(request):
    return render(request, 'saludo.html', {
        'titulo':'Bienvenidos a la UNTELS',
        'mensaje':'Proyecto para Examen Final'
    })

def crear_producto(request):

    return render(request, 'crear_producto.html', {
        'titulo':'Crear producto',
        'producto':""
    })

def crear_curso(request):

    return render(request, 'crear_curso.html', {
        'titulo':'Crear producto',
        'curso':""
    })