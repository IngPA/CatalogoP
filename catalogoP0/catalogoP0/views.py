from django.shortcuts import render

from productosP.models import Producto

def mifuncion_inicio(request):
    template_name = "index.html"

    #========================================
    # query en django utilizando orm

    p= Producto.objects.create(
        nombre= "remera",
        precio= 1500,
        descripcion= "remera barata"
    )
    contexto = {
        'productos_probando' : "art1, art2"
    }
    return render(request, template_name, contexto)