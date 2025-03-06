from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from .models import Projetos


@receiver(m2m_changed, sender=Projetos.equipe.through)
def atualizar_qtd_equipe(sender, instance, action):
    if action in ['post_add', 'post_remove']:
        instance.qtd_membros = instance.equipe.count()
        instance.save()