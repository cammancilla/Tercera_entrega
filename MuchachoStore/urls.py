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

    # * --------- Pagina de Administrador ---------------
    path('indexAdmin/', views.indexAdmin, name='indexAdmin'),
    # * ------------------------------------------------

    
    # * --------- Paginas de Productos -----------------
    path('parlantesec/', views.indexParlantesec, name='parlantesec'),
    path('pendrivesec/', views.indexPendrivesec, name='pendrivesec'),
    path('audifonosec/', views.indexAudifonosec, name='audifonosec'),
    # * ------------------------------------------------

    # * --------- Pagina de Servicios -------------------
    path('servicios/', views.indexServicios, name='servicios'),
    # * ------------------------------------------------

    # * --------- ACCOUNTS ---------------------
    
    # * ----------C-R-U-D----------------------

    path('producto_create/', views.crearProducto, name='producto_create'),
    path('producto_update/<str:pk>/', views.actualizarProducto, name='producto_update'),
    path('producto_delete/<str:pk>/', views.eliminarProducto, name='producto_delete'),

]