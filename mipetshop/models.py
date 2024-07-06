
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Modelo de usuario personalizado
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    edad = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre        

class Categoria(models.Model):
    """
    Modelo de categoría de productos
    """
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class Producto(models.Model):
    """
    Modelo de producto
    """
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Compra(models.Model):
    """
    Modelo de compra
    """
    fecha_compra = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    forma_pago = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class Carrito(models.Model):
    """
    Modelo de carrito de compras
    """
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class CarritoItem(models.Model):
    """
    Modelo de item del carrito de compras
    """
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
# Create your models here.

