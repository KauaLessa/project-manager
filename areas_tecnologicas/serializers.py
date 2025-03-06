from rest_framework import serializers
from .models import AreasTecnologicas


class AreasTecnologicasSerializer(serializers.ModelSerializer):
    id_area_tecnologica = serializers.IntegerField(read_only=True)


    class Meta:
        model = AreasTecnologicas
        fields = ['id_area_tecnologica', 'area_tecnologica']