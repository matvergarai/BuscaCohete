from django.shortcuts import render, redirect
from rest_framework import generics
from .models import SitiosBloqueados
from .serializers import SitiosBloqueadosSerializer
from .forms import SitiosBloqueadosForm

def bloquear_sitio(request):
    if request.method == 'POST':
        form = SitiosBloqueadosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bloquearsitio')  # Redirige a donde quieras después de procesar el formulario
    else:
        form = SitiosBloqueadosForm()
    return render(request, 'core/formulario_sitio_bloqueado.html', {'form': form})


class SitiosBloqueadosListView(generics.ListAPIView):
    queryset = SitiosBloqueados.objects.all()
    serializer_class = SitiosBloqueadosSerializer

def home(request):
    # Lógica para la vista de la página de inicio
    return render(request, 'core/home.html')


def login(request):
    # Lógica para la vista de inicio de sesión
    return render(request, 'core/login.html')

def register(request):
    # Lógica para la vista de registro
    return render(request, 'core/register.html')

def forgot_password(request):
    # Lógica para la vista de olvido de contraseña
    return render(request, 'core/forgot_password.html')

def reset_password(request):
    # Lógica para la vista de restablecimiento de contraseña
    return render(request, 'core/reset_password.html')

def dashboard(request):
    # Lógica para la vista del panel de control
    return render(request, 'core/dashboard.html')

def navigation_profiles(request):
    # Lógica para la vista de perfiles de navegación
    return render(request, 'core/navigation_profiles.html')

def edit_navigation_profile(request):
    # Lógica para la vista de edición de perfil de navegación
    return render(request, 'core/edit_navigation_profile.html')

def delete_navigation_profile(request):
    # Lógica para la vista de eliminación de perfil de navegación
    return render(request, 'core/delete_navigation_profile.html')

def filters(request):
    # Lógica para la vista de filtros
    return render(request, 'core/filters.html')

def history(request):
    # Lógica para la vista de historial
    return render(request, 'core/history.html')

def stats(request):
    # Lógica para la vista de estadísticas
    return render(request, 'core/stats.html')

def user_profile(request):
    # Lógica para la vista del perfil de usuario
    return render(request, 'core/user_profile.html')

def change_password(request):
    # Lógica para la vista de cambio de contraseña
    return render(request, 'core/change_password.html')

def about_us(request):
    # Lógica para la vista de "Acerca de nosotros"
    return render(request, 'core/about_us.html')

def contact_us(request):
    # Lógica para la vista de "Contáctanos"
    return render(request, 'core/contact_us.html')
