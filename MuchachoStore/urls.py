from Tercera_entrega.urls import path
from . import views

urlpatterns = [
    # * --------- Paginas Principales -------------------
    path('', views.indexPrincipal, name='indexPrincipal'),
    path('indexContacto/', views.indexContacto, name='indexContacto'),
    # * ------------------------------------------------
    
    # * --------- Pagina de Especificaciones -----------
    path('especificacion/', views.indexEspecificacion, name='especificacion'),
    # * ------------------------------------------------

    # * --------- Pagina de Login y Registro ------------
    path('login/', views.indexLogin, name='login'),
    path('registro/', views.indexRegistro, name='registro'),
    #* -------------------------------------------------
    
    # * --------- Paginas de Productos -----------------
    path('parlantesec/', views.indexParlantesec, name='parlantesec'),
    path('pendrivesec/', views.indexPendrivesec, name='pendrivesec'),
    path('audifonosec/', views.indexAudifonosec, name='audifonosec'),
    # * ------------------------------------------------

    # * --------- Pagina de Servicios -------------------
    path('servicios/', views.indexServicios, name='servicios'),
    # * ------------------------------------------------

    # * --------- ACCOUNTS ---------------------
    

]