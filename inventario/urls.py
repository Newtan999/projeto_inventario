from django.urls import path, include

urlpatterns = [
    path('equipamentos/', include('inventario.equipamento.urls')),
    path('setores/', include('inventario.setor.urls')),
    path('manutencoes/', include('inventario.manutencao.urls')),
]
