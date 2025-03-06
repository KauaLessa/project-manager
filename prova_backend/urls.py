from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('colaboradores/', include('colaboradores.urls')),
    path('financiadores/', include('financiadores.urls')),
    path('areas-tecnologicas/', include('areas_tecnologicas.urls')),
    path('projetos/', include('projetos.urls'))
]
