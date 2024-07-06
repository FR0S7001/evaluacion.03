from django.urls import path
from .views import index, alimento_seco_gato, alimento_humedo_gato, alimento_perro, accesorios, api
from .views import cliente_list,cliente_create,cliente_delete,cliente_detail,cliente_update,compra_create,compra_delete,compra_detail,compra_list,compra_update,mascota_create,mascota_delete,mascota_detail,mascota_list,mascota_update,producto_create,producto_delete,producto_detail,producto_list,producto_update,detallecompra_create,detallecompra_delete,detallecompra_detail,detallecompra_list,detallecompra_update

urlpatterns = [
    path('', index, name='index'),
    path('alimento-seco-gato', alimento_seco_gato, name='alimento_seco_gato'),
    path('alimento-humedo-gato/', alimento_humedo_gato, name='alimento_humedo_gato'),
    path('alimento-perro/', alimento_perro, name='alimento_perro'),
    path('accesorios/', accesorios, name='accesorios'),
    path('api/', api, name='api'),

    # ... other URLs ...
    path('clientes/', cliente_list, name='cliente_list'),
    path('clientes/<int:pk>/', cliente_detail, name='cliente_detail'),
    path('clientes/create/', cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/update/', cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/delete/', cliente_delete, name='cliente_delete'),

    path('mascotas/', mascota_list, name='mascota_list'),
    path('mascotas/<int:pk>/', mascota_detail, name='mascota_detail'),
    path('mascotas/create/', mascota_create, name='mascota_create'),
    path('mascotas/<int:pk>/update/', mascota_update, name='mascota_update'),
    path('mascotas/<int:pk>/delete/', mascota_delete, name='mascota_delete'),

    path('productos/', producto_list, name='producto_list'),
    path('productos/<int:pk>/', producto_detail, name='producto_detail'),
    path('productos/create/', producto_create, name='producto_create'),
    path('productos/<int:pk>/update/', producto_update, name='producto_update'),
    path('productos/<int:pk>/delete/', producto_delete, name='producto_delete'),

    path('compras/', compra_list, name='compra_list'),
    path('compras/<int:pk>/', compra_detail, name='compra_detail'),
    path('compras/create/', compra_create, name='compra_create'),
    path('compras/<int:pk>/update/',compra_update, name='compra_update'),
    path('compras/<int:pk>/delete/', compra_delete, name='compra_delete'),

    path('detallecompras/', detallecompra_list, name='detallecompra_list'),
    path('detallecompras/<int:pk>/', detallecompra_detail, name='detallecompra_detail'),
    path('detallecompras/create/', detallecompra_create, name='detallecompra_create'),
    path('detallecompras/<int:pk>/update/', detallecompra_update, name='detallecompra_update'),
    path('detallecompras/<int:pk>/delete/', detallecompra_delete, name='detallecompra_delete'),
]

