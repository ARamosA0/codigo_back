from django.contrib import admin

# Register your models here.
from .models import Categoria, PedidoDetalle,Producto,Cliente,Pedido

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(PedidoDetalle)