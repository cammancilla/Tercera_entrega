from django.shortcuts import render
from .models import *


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
    return render(request, 'indexAdmin.html')

