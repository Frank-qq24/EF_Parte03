from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from miapp.models import producto
from datetime import datetime

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
    productos=producto(
    codigo          = "5",
    nombre          = "limon",
    precio_compra   = "3",
    precio_venta    = "4",
    Fecha_compra    = f" {datetime.today().strftime('%Y-%m-%d')}",
    Fecha_registro = f" {datetime.today().strftime('%Y-%m-%d')}",
    estado   = "A"
    )
    productos.save()

    return render(request, 'crear_producto.html', {
        'titulo':'Crear producto',
        'producto':
        f"Producto registrado:"+
        f"//codigo: {productos.codigo} // nombre: {productos.nombre} // precio_compra: {productos.precio_compra} //"+
        f"precio_venta: {productos.precio_venta} // Fecha_compra: {productos.Fecha_compra} // Fecha_de_registro: {productos.Fecha_registro}"+
        f"// Estado:{productos.estado}"
    })

def crear_curso(request):

    return render(request, 'crear_curso.html', {
        'titulo':'Crear producto',
        'curso':""
    })