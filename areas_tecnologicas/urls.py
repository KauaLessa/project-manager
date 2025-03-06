from django.urls import path
from .views import AreasTecnologicasViewSet


tec_list = AreasTecnologicasViewSet.as_view({'get':'list'})
tec_create = AreasTecnologicasViewSet.as_view({'post':'create'})
tec_patch = AreasTecnologicasViewSet.as_view({'patch':'partial_update'})
tec_delete = AreasTecnologicasViewSet.as_view({'delete': 'destroy'})

urlpatterns = [
    path('listar', tec_list, name='tec-list'),
    path('cadastrar', tec_create, name='tec-create'),
    path('<int:pk>/editar', tec_patch, name='tec-patch'),
    path('<int:pk>/excluir', tec_delete, name='tec-delete')
]