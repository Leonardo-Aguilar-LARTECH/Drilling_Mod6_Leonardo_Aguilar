from django.urls import path
from . import views

urlpatterns = [
    #path('vehiculos', views.IndexView, name='vehiculos'),
    path('vehiculo/add', views.AddVehicleView.as_view(), name='add'),
    path('vehiculo/list', views.VehiculosView.as_view(), name='list'),
]
