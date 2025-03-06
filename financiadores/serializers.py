from rest_framework import serializers
from .models import Financiadores

class FinanciadoresSerializer(serializers.ModelSerializer):
    id_financiador = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Financiadores
        fields = ['id_financiador', 'financiador']