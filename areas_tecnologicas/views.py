from rest_framework import viewsets
from .models import AreasTecnologicas
from .serializers import AreasTecnologicasSerializer


class AreasTecnologicasViewSet(viewsets.ModelViewSet):
    queryset = AreasTecnologicas.objects.all()
    serializer_class = AreasTecnologicasSerializer
