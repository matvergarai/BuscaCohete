from django import forms
from .models import SitiosBloqueados

class SitiosBloqueadosForm(forms.ModelForm):
    class Meta:
        model = SitiosBloqueados
        fields = ['url', 'bloqueoInteligente', 'idSupervisor']
