from rest_framework import serializers
from .models import Projetos


class ProjetosSerializer(serializers.ModelSerializer):
    id_projeto = serializers.IntegerField(read_only=True)
    qtd_membros = serializers.IntegerField(read_only=True)

    class Meta:
        model = Projetos
        fields = '__all__'

    def validate(self, data):
        if data['inicio_vigencia'] >= data['fim_vigencia']:
            error_msg = "Data de fim deve ocorrer após a data de início."
            raise serializers.ValidationError(error_msg)
        return data