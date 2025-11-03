from django.urls import path
from . import views

app_name = 'setor'

urlpatterns = [
    path('', views.listar_setor, name='listar_setor'),
    path('cadastrar/', views.cadastrar_setor, name='cadastrar_setor'),
    path('editar/<int:setor_id>/', views.editar_setor, name='editar_setor'),
    path('excluir/<int:setor_id>/', views.excluir_setor, name='excluir_setor'),

]