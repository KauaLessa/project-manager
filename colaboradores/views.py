from rest_framework import viewsets
from .models import Colaboradores
from .serializers import ColaboradoresSerializer

class ColaboradoresViewSet(viewsets.ModelViewSet):
    queryset = Colaboradores.objects.all()
    serializer_class = ColaboradoresSerializer