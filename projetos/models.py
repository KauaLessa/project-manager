from django.db import models
from financiadores.models import Financiadores
from areas_tecnologicas.models import AreasTecnologicas
from colaboradores.models import Colaboradores
from django.core.exceptions import ValidationError


class Projetos(models.Model):
    id_projeto = models.IntegerField(primary_key=True)
    projeto = models.CharField(max_length=100)
    id_financiador = models.ForeignKey(
        Financiadores, 
        blank=True, 
        null=True,
        on_delete=models.SET_NULL
    )
    id_area_tecnologica = models.ForeignKey(
        AreasTecnologicas,
        blank=True, 
        null=True,
        on_delete=models.SET_NULL
    )
    equipe = models.ManyToManyField(
        Colaboradores,
        through='Equipe',
        related_name='projetos',
        blank=True
    )
    ativo = models.BooleanField()
    inicio_vigencia = models.DateField()
    fim_vigencia = models.DateField()
    valor =  models.DecimalField(max_digits=10, decimal_places=2)
    qtd_membros = models.IntegerField(default=0)

    def clean(self, *args, **kwargs):
        if self.inicio_vigencia >= self.fim_vigencia:
            error_msg = "Data de fim deve ocorrer após a data de início."
            raise ValidationError(error_msg)
        
        super().clean(*args, **kwargs)

        
class Equipe(models.Model):
    projeto = models.ForeignKey(
        Projetos,
        on_delete=models.CASCADE,
        related_name='equipes'
    )
    colaborador = models.ForeignKey(Colaboradores, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('projeto', 'colaborador')