from Tercera_entrega.urls import path
from . import views

urlpatterns = [
    path('', views.indexPrincipal, name='indexPrincipal'),
    path('indexContacto/', views.indexContacto, name='indexContacto'),
    path('audifonosec/', views.indexAudifonosec, name='audifonosec'),
    path('especificacion/', views.indexEspecificacion, name='especificacion'),
    path('login/', views.indexLogin, name='login'),
    path('registro/', views.indexRegistro, name='registro'),
    path('parlantesec/', views.indexParlantesec, name='parlantesec'),
    path('pendrivesec/', views.indexPendrivesec, name='pendrivesec'),
    path('servicios/', views.indexServicios, name='servicios'),
    

]