from django.shortcuts import render

def mifuncion_inicio(request):
    template_name = "index.html"
    contexto = {
        'productos_mios' : 'art1, art2'
    }
    return render(request, template_name, contexto)