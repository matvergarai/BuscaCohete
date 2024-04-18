from rest_framework import serializers
from .models import SitiosBloqueados

class SitiosBloqueadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SitiosBloqueados
        fields = '__all__'