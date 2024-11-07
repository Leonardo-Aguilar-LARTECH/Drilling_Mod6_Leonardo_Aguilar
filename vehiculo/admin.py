from django.contrib import admin
from .models import Vehiculo

# Register your models here.

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    search_fields = ['marca', 'modelo', 'categoria']
    list_display = ['marca', 'modelo', 'categoria', 'precio']
    ordering = ['marca']
    list_filter = ['categoria', 'marca', 'precio']
