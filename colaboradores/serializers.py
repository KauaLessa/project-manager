from .models import Colaboradores
from rest_framework import serializers
from validate_docbr import CPF

class ColaboradoresSerializer(serializers.ModelSerializer):
    id_colaborador = serializers.IntegerField(read_only=True)
    dt_nascimento = serializers.DateField()


    class Meta:
        model = Colaboradores
        fields = ['id_colaborador', 'cpf', 'nome', 'dt_nascimento']


    def validate_cpf(self, value):
        cpf = CPF()
        if not cpf.validate(value):
            raise serializers.ValidationError('CPF inválido.')
        return value
