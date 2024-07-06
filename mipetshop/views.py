from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cliente, Mascota, Producto, Compra, DetalleCompra
from .forms import ClienteForm, MascotaForm, ProductoForm, CompraForm, DetalleCompraForm

# Create your views here.
def index(request):
    return render(request, 'mipetshop/index.html')

def alimento_seco_gato(request):
    return render(request, 'mipetshop/alimento_seco_gato.html')

def alimento_humedo_gato(request):
    return render(request, 'mipetshop/alimento_humedo_gato.html')

def alimento_perro(request):
    return render(request, 'mipetshop/alimento_perro.html')

def accesorios(request):
    return render(request, 'mipetshop/accesorios.html')

def api(request):
    return render(request, 'mipetshop/api.html')

# Vistas para Clientes
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'mipetshop/cliente_list.html', {'clientes': clientes})

def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'mipetshop/cliente_detail.html', {'cliente': cliente})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'mipetshop/cliente_form.html', {'form': form})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'mipetshop/cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'mipetshop/cliente_confirm_delete.html', {'cliente': cliente})

# Vistas para Mascotas
def mascota_list(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mipetshop/mascota_list.html', {'mascotas': mascotas})

def mascota_detail(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    return render(request, 'mipetshop/mascota_detail.html', {'mascota': mascota})

def mascota_create(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascota_list')
    else:
        form = MascotaForm()
    return render(request, 'mipetshop/mascota_form.html', {'form': form})

def mascota_update(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('mascota_list')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'mipetshop/mascota_form.html', {'form': form})

def mascota_delete(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota_list')
    return render(request, 'mipetshop/mascota_confirm_delete.html', {'mascota': mascota})

# Vistas para Productos
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'mipetshop/producto_list.html', {'productos': productos})

def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'mipetshop/producto_detail.html', {'producto': producto})

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'mipetshop/producto_form.html', {'form': form})

def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'mipetshop/producto_form.html', {'form': form})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'mipetshop/producto_confirm_delete.html', {'producto': producto})

# Vistas para Compras
def compra_list(request):
    compras = Compra.objects.all()
    return render(request, 'mipetshop/compra_list.html', {'compras': compras})

def compra_detail(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    return render(request, 'mipetshop/compra_detail.html', {'compra': compra})

def compra_create(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compra_list')
    else:
        form = CompraForm()
    return render(request, 'mipetshop/compra_form.html', {'form': form})

def compra_update(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('compra_list')
    else:
        form = CompraForm(instance=compra)
    return render(request, 'mipetshop/compra_form.html', {'form': form})

def compra_delete(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    if request.method == 'POST':
        compra.delete()
        return redirect('compra_list')
    return render(request, 'mipetshop/compra_confirm_delete.html', {'compra': compra})

# Vistas para Detalles de Compra
def detallecompra_list(request):
    detallecompras = DetalleCompra.objects.all()
    return render(request, 'mipetshop/detallecompra_list.html', {'detallecompras': detallecompras})

def detallecompra_detail(request, pk):
    detallecompra = get_object_or_404(DetalleCompra, pk=pk)
    return render(request, 'mipetshop/detallecompra_detail.html', {'detallecompra': detallecompra})

def detallecompra_create(request):
    if request.method == 'POST':
        form = DetalleCompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detallecompra_list')
    else:
        form = DetalleCompraForm()
    return render(request, 'mipetshop/detallecompra_form.html', {'form': form})

def detallecompra_update(request, pk):
    detallecompra = get_object_or_404(DetalleCompra, pk=pk)
    if request.method == 'POST':
        form = DetalleCompraForm(request.POST, instance=detallecompra)
        if form.is_valid():
            form.save()
            return redirect('detallecompra_list')
    else:
        form = DetalleCompraForm(instance=detallecompra)
    return render(request, 'mipetshop/detallecompra_form.html', {'form': form})

def detallecompra_delete(request, pk):
    detallecompra = get_object_or_404(DetalleCompra, pk=pk)
    if request.method == 'POST':
        detallecompra.delete()
        return redirect('detallecompra_list')
    return render(request, 'mipetshop/detallecompra_confirm_delete.html', {'detallecompra': detallecompra})