from .views import ProjetosViewSet, ProjetosForm
from django.urls import path


projeto_listar = ProjetosViewSet.as_view({'get':'list'})
projeto_cadastrar = ProjetosViewSet.as_view({'post':'create'})
projeto_inativar = ProjetosViewSet.as_view({'post':'inativar'})
projeto_editar = ProjetosViewSet.as_view({'patch':'partial_update'})
projeto_vizualizar = ProjetosViewSet.as_view({'get':'retrieve'})
projeto_equipe = ProjetosViewSet.as_view({'get':'equipe'})
projeto_atualizar_equipe = ProjetosViewSet.as_view({'patch':'atualizar_equipe'})

urlpatterns = [
    path('listar', projeto_listar, name='projeto-listar'),
    path('cadastrar', projeto_cadastrar, name='cadastrar-projeto'),
    path('<int:pk>/inativar', projeto_inativar, name='inativar-projeto'),
    path('<int:pk>/editar', projeto_editar, name='editar-projeto'),
    path('<int:pk>/visualizar', projeto_vizualizar, name='visualizar-projeto'),
    path('<int:pk>/equipe', projeto_equipe, name='projeto-equipe'),
    path('<int:pk>/equipe/atualizar', projeto_atualizar_equipe, name='atualizar-equipe'),
    path('form', ProjetosForm.as_view(), name='projeto-form')
]