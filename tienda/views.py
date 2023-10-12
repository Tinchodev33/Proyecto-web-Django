from django.shortcuts import render
from tienda.models import Producto 
from.forms import ContactoForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def menu_button(request):
    return HttpResponseRedirect(reverse('nombre_de_tu_url'))


def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def somos(request):
    return render(request, 'somos.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = ""
        else:
            data["form"] = formulario
            
    response = render(request, 'Contacto.html', data)
    
    response.set_cookie('estoy', 'en_linea')
    
    return response

def busqueda(request):
    if "buscar" in request.GET and request.GET["buscar"]:
        consulta = request.GET["buscar"] 
        productos = Producto.objects.filter(nombre__icontains=consulta)
        return render(request, 'resultados.html', {'productos': productos})
    else:
        return render(request, 'resultados.html')
    
