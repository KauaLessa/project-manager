from django.urls import path
from .views import FinanciadoresViewSet


finac_list = FinanciadoresViewSet.as_view({'get':'list'})
finac_create = FinanciadoresViewSet.as_view({'post':'create'})
finac_patch = FinanciadoresViewSet.as_view({'patch':'partial_update'})
finac_delete = FinanciadoresViewSet.as_view({'delete': 'destroy'})

urlpatterns = [
    path('listar', finac_list, name='finac-list'),
    path('cadastrar', finac_create, name='finac-create'),
    path('<int:pk>/editar', finac_patch, name='finac-patch'),
    path('<int:pk>/excluir', finac_delete, name='finac-delete')
]
