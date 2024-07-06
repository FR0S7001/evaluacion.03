from django import forms
from .models import Cliente, Mascota, Producto, Compra, DetalleCompra

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'

class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = '__all__'