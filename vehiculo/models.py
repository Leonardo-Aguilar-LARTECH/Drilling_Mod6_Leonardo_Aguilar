from django.db import models
from django.forms import ValidationError

# Create your models here.

class Vehiculo(models.Model):
        
    MARCAS = [
        ('FIAT', 'Fiat'),
        ('CHEVROLET', 'Chevrolet'),
        ('FORD', 'Ford'),
        ('TOYOTA', 'Toyota'),
    ]
    CATEGORIAS = [
        ('PARTICULAR', 'Particular'),
        ('TRANSPORTE', 'Transporte'),
        ('CARGA', 'Carga'),
    ]
        
    marca = models.CharField(max_length=20, blank=False, null=False, choices=MARCAS, default='FORD')
    modelo = models.CharField(max_length=100, blank=False, null=False)
    serial_carroceria = models.CharField(max_length=50, blank=False, null=False)
    serial_motor = models.CharField(max_length=50, blank=False, null=False)
    categoria = models.CharField(max_length=20, blank=False, null=False, choices=CATEGORIAS, default='PARTICULAR')
    precio = models.PositiveSmallIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_modificacion = models.DateTimeField(auto_now_add = False, auto_now = True)


    def clean(self) -> None:
        if self.precio <=0:
            raise ValidationError("El Precio de Venta debe Ser un valor positivo superior a $0")
    
    def __str__(self) -> str:
        return f"{self.marca} {self.modelo}"
    
    class Meta:
        permissions = [
            ("visualizar_catalogo", "Puede Visualizar el catalogo"),
            ("add_vehiculomodel", "Puede Agregar Nuevos Vehiculos"),
        ]
