from django.contrib import admin
from .models import Producto, Cliente, Pedido, Comentario
# Register your models here.

try:
    admin.site.unregister(Producto)
except admin.sites.NotRegistered:
    pass

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_formateado')

    def precio_formateado(self, obj):
        return "${}".format(obj.precio)



admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Comentario)