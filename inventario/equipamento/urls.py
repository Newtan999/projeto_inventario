from django.urls import path
from . import views

app_name = 'equipamento'

urlpatterns = [
    path('', views.listar_equipamento, name='listar_equipamento'),
    path('novo/', views.cadastrar_equipamento, name='cadastrar_equipamento'),
    path('editar/<int:id>/', views.editar_equipamento, name='editar_equipamento'),
    path('excluir/<int:id>/', views.excluir_equipamento, name='excluir_equipamento'),

]