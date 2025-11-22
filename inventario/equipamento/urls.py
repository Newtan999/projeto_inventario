from django.urls import path
from . import views
from .views import ExcluirEquipamentoView

app_name = 'equipamento'

urlpatterns = [
    path('', views.listar_equipamentos, name='listar_equipamentos'),
    path('novo/', views.cadastrar_equipamento, name='form_equipamentos'),
   # path('editar/<int:id>/', views.editar_equipamento, name='editar_equipamento'),
    path('excluir/<int:id>/', ExcluirEquipamentoView.as_view, name='excluir_equipamento'),

]