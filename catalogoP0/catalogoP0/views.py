from django.shortcuts import render

from productosP.models import Producto

def mifuncion_inicio(request):
    template_name = "index.html"
    """
    #========================================
    # query en django utilizando orm

    p= Producto.objects.create(
        nombre= "Pantalon",
        precio= 2000,
        descripcion= "Pantalon azul"
    )
    """
    productos = Producto.objects.all()
   
    contexto = {
        'productos' : productos,
        'nombre' : "Lucas?"
    }
    return render(request, template_name, contexto)