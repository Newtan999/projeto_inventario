from django.urls import path
from . import views
from .views import ExcluirSetorView


app_name = 'setor'

urlpatterns = [
    path('', views.listar_setores, name='listar_setores'),
    path('cadastrar/', views.cadastrar_setor, name='cadastrar_setor'),
    path('editar/<int:pk>/', views.editar_setor, name='editar_setor'),
    path('excluir/<int:pk>/', ExcluirSetorView.as_view(), name='excluir_setor'),

]