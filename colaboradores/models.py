from django.db import models
from validate_docbr import CPF
from django.core.exceptions import ValidationError


def validate_cpf(value):
        cpf = CPF()
        if not cpf.validate(value):
            raise ValidationError('CPF inválido.')


class Colaboradores(models.Model):
    id_colaborador = models.IntegerField(primary_key=True)
    cpf = models.CharField(
        max_length=14,
        verbose_name='CPF',
        validators=[validate_cpf], 
        unique=True
    )
    nome = models.CharField(max_length=100)
    dt_nascimento = models.DateField(verbose_name='Data de nascimento')

    def __str__(self):
        return f'{self.cpf} {self.nome}'