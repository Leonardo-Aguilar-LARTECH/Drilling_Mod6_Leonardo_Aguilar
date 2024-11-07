from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.models import Permission

class UserRegistroView(CreateView):
    form_class =  UserCreationForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        
        response = super().form_valid(form)
        usuario = form.instance 
        permiso = Permission.objects.get(codename='visualizar_catalogo') 
        usuario.user_permissions.add(permiso) 
        usuario.save()

        messages.success(self.request, 'Usuario Registrado con Exito.')
        return response
    
class UserLoginView(LoginView):
    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        
        messages.success(self.request, 'Sesion Iniciada con Exito.')
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return self.get_redirect_url() or self.success_url
    
class UserLogoutView(LogoutView):
    next_page = 'index'
    
    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, 'Secion Cerrada con Exito.')
        return super().dispatch(request, *args, **kwargs)
    