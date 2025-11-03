from django.db import models
from inventario.setor.models import Setor

# Equipamento
class Equipamento(models.Model):
    TIPO_EQUIPAMENTO = [
        ('desktop', 'Desktop'),
        ('notebook', 'Notebook'),
        ('monitor', 'Monitor'),
        ('servidor', 'Servidor'),
        ('nobreak', 'Nobreak'),
        ('impressora', 'Impressora'),
        ('outro', 'Outro'),
    ]

    descricao = models.CharField(max_length = 100)
    data_aquisicao = models.DateField()
    responsavel = models.CharField(max_length = 100, blank=True, null=True)
    status = models.CharField(max_length = 30, default = 'Em uso')
    numero_patrimonio = models.CharField(max_length=9, unique = True)
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao
    