from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ProductoForm, ComentarioForm


# Create your views here.

def indexPrincipal(request):
    return render(request, 'indexprincipal.html')

def indexContacto(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu comentario ha sido enviado exitosamente.')
            return redirect('indexContacto')
    else:
        form = ComentarioForm()
    return render(request, 'indexContacto.html', {'form': form})

def indexAudifonosec(request):
    return render(request, 'audifonosec.html')

def indexEspecificacion(request):
    return render(request, 'especificacion.html')

def indexLogin(request):
    if request.method == 'POST':
        email = request.POST.get('correo')
        password = request.POST.get('passwordLogin')
        
        # Buscar usuario por email en lugar de username
        from django.contrib.auth.models import User
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Bienvenido! Has iniciado sesión exitosamente.')
                return redirect('indexAdmin')
            else:
                messages.error(request, 'Credenciales incorrectas.')
        except User.DoesNotExist:
            messages.error(request, 'No existe una cuenta con este correo electrónico.')
    
    return render(request, 'login.html')

def indexRegistro(request):
    return render(request, 'registro.html')

def indexLogout(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('indexPrincipal')

def indexParlantesec(request):
    return render(request, 'parlantesec.html')

def indexPendrivesec(request):
    return render(request, 'pendrivesec.html')

def indexServicios(request):
    return render(request, 'servicios.html')

@login_required
def indexAdmin(request):
    productos = Producto.objects.all()
    return render(request, 'indexAdmin.html', {'productos':productos})

def crearProducto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('indexAdmin')
    else:
        form = ProductoForm()
    return render(request, 'productoCrear.html', {'form':form})

def actualizarProducto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('indexAdmin')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productoModificar.html', {'form': form, 'producto': producto})
    
def eliminarProducto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
    return redirect('indexAdmin')