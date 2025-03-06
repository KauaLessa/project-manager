from django.urls import path
from .views import ColaboradoresViewSet


colab_list = ColaboradoresViewSet.as_view({'get':'list'})
colab_create = ColaboradoresViewSet.as_view({'post':'create'})
colab_patch = ColaboradoresViewSet.as_view({'patch':'partial_update'})
colab_retrieve = ColaboradoresViewSet.as_view({'get':'retrieve'})
colab_delete = ColaboradoresViewSet.as_view({'delete': 'destroy'})

urlpatterns = [
    path('listar', colab_list, name='colab-list'),
    path('cadastrar', colab_create, name='colab-create'),
    path('<int:pk>/vizualizar', colab_retrieve, name='colab-retrieve'),
    path('<int:pk>/editar', colab_patch, name='colab-patch'),
    path('<int:pk>/excluir', colab_delete, name='colab-delete')
]

