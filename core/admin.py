from django.contrib import admin
from .models import Supervisor

@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    # Define cómo se mostrarán los datos en el panel de administración
    list_display = ['idSupervisor', 'nombreSupervisor', 'correo', 'controlParentalActivado', 'gradoBloqueoImagen']
    search_fields = ['nombreSupervisor', 'correo']  # Campos por los que se puede buscar
