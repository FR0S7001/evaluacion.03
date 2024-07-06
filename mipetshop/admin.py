from django.contrib import admin
from mipetshop.models import Cliente, Mascota, Producto, Compra

# Registro de modelos en el panel de administración
admin.site.register(Cliente)
admin.site.register(Mascota)
admin.site.register(Producto)
admin.site.register(Compra)