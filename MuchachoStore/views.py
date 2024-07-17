from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ProductoForm


# Create your views here.

def indexPrincipal(request):
    return render(request, 'indexprincipal.html')

def indexContacto(request):
    return render(request, 'indexContacto.html')

def indexAudifonosec(request):
    return render(request, 'audifonosec.html')

def indexEspecificacion(request):
    return render(request, 'especificacion.html')

def indexLogin(request):

    if request.method == 'GET':
        print('GET')
    else:
        print('POST')


    return render(request, 'login.html')

def indexRegistro(request):
    return render(request, 'registro.html')

def indexParlantesec(request):
    return render(request, 'parlantesec.html')

def indexPendrivesec(request):
    return render(request, 'pendrivesec.html')

def indexServicios(request):
    return render(request, 'servicios.html')

def indexAdmin(request):
    productos = Producto.objects.all()
    return render(request, 'indexAdmin.html', {'productos':productos})

def crearProducto(request):
    producto = Producto.objects.get
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = Producto(
                nombre = form.cleaned_data['nombre'],
                descripcion = form.cleaned_data['descripcion'],
                precio = form.cleaned_data['precio'],
                stock = form.cleaned_data['stock'],
                categoria = form.cleaned_data['categoria'],
            )
            producto.save()

            return redirect('indexAdmin')
    else:
        form = ProductoForm()
    return render(request, 'productoCrear.html', {'form':form})

def actualizarProducto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto.nombre = form.cleaned_data['nombre']
            producto.descripcion = form.cleaned_data['descripcion']
            producto.precio = form.cleaned_data['precio']
            producto.stock = form.cleaned_data['stock']
            producto.categoria = form.cleaned_data['categoria']
            producto.save()

            return redirect('indexAdmin')
    else:
        form = ProductoForm(initial={
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'stock': producto.stock,
            'categoria': producto.categoria,
        })
    return render(request, 'productoModificar.html', {'form': form})
    
def eliminarProducto(request, pk):
    context = {}
    try:
        producto = Producto.objects.get(id=pk)
        producto.delete()
        productos = Producto.objects.all()
        context = {'productos':productos}
        return render(request, 'indexAdmin.html', context)
    except Producto.DoesNotExist:
        productos = Producto.objects.all()
        context = {'productos':productos}
        return render(request, 'indexAdmin.html', context)