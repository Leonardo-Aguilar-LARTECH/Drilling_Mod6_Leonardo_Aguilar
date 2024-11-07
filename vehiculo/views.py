from django.shortcuts import redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages

from .models import Vehiculo
# Create your views here.

class AddVehicleView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Vehiculo
    template_name = "vehiculo/add.html"
    fields = ['marca', 'modelo', 'serial_carroceria','serial_motor','categoria','precio']
    success_url = reverse_lazy('index')
    permission_required = 'vehiculo.add_vehiculomodel'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, "Usted no tiene el nivel de acceso para acceder a la vista.")
            return redirect("index")
        
        else:
            messages.info(self.request, "Primero debe iniciar sesión para continuar.")
            return redirect("login")
        
class VehiculosView(ListView):
    model = Vehiculo
    template_name = "vehiculo/list.html"
    context_object_name = 'vehiculos'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        for vehiculo in context['vehiculos']:
            if vehiculo.precio < 10000:
                vehiculo.condicion_precio = 'Bajo'
            elif 10000 <= vehiculo.precio <= 30000:
                vehiculo.condicion_precio = 'Medio'
            else:
                vehiculo.condicion_precio = 'Alto'
                
        return context
    
    