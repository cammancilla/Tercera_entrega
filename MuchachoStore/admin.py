from django.contrib import admin
from .models import Producto, Cliente, Pedido, Comentario

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_formateado', 'stock', 'categoria', 'created_at')
    list_filter = ('categoria', 'created_at')
    search_fields = ('nombre', 'descripcion', 'categoria')
    readonly_fields = ('created_at', 'updated_at')

    def precio_formateado(self, obj):
        return f"${obj.precio:,.2f}"
    precio_formateado.short_description = "Precio"

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'created_at')
    search_fields = ('nombre', 'apellido', 'email')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'total_formateado', 'fecha')
    list_filter = ('fecha',)
    readonly_fields = ('fecha',)

    def total_formateado(self, obj):
        return f"${obj.total:,.2f}"
    total_formateado.short_description = "Total"

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('nombre', 'email', 'mensaje')
    readonly_fields = ('created_at',)