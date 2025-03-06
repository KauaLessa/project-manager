from rest_framework import viewsets
from .models import Financiadores
from .serializers import FinanciadoresSerializer


class FinanciadoresViewSet(viewsets.ModelViewSet):
    queryset = Financiadores.objects.all()
    serializer_class = FinanciadoresSerializer
