from django.urls import path
from . import views

app_name = 'manutencao'

urlpatterns = [
    path('', views.listar_manutencoes, name='listar_manutencoes' ),
    path('novo/', views.cadastrar_manutencao, name='cadastrar_equipamento'),
    #path('editar/<int:id>/', views.editar_manutencao, name='editar_equipamento'),
    #path('excluir/<int:id>/', views.excluir_manutencao, name='excluir_equipamento'),

]
