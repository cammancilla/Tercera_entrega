from django.db import models

# Create your models here.
# Modelo par genero

# Modelo para categoria

# Modelo para producto
# Precio NUMERICO

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos', blank=True, null=True)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    
# Modelo para cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
# Modelo para pedido
class Pedido(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    
# Modelo para comentario para mejorar la experiencia del cliente
class Comentario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
    

    
