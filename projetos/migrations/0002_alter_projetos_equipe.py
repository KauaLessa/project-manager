# Generated by Django 5.1.6 on 2025-03-04 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0004_alter_colaboradores_cpf'),
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetos',
            name='equipe',
            field=models.ManyToManyField(blank=True, null=True, related_name='projetos', through='projetos.Equipe', to='colaboradores.colaboradores'),
        ),
    ]
