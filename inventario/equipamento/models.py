from django.db import models
from inventario.setor.models import Setor

# Equipamento
class Equipamento(models.Model):
    TIPO_EQUIPAMENTO = [
        ('desktop', 'Desktop'), #(nome, texto exibido)
        ('notebook', 'Notebook'),
        ('monitor', 'Monitor'),
        ('servidor', 'Servidor'),
        ('nobreak', 'Nobreak'),
        ('impressora', 'Impressora'),
        ('outro', 'Outro'),
    ]
    
    STATUS = [
        ('em_uso', 'Em uso'),
        ('obsoleto', 'Obsoleto'),
        ('com_defeito', 'Com defeito'),
    ]

    descricao = models.CharField(max_length = 100)
    tipo = models.CharField(max_length=20, choices=TIPO_EQUIPAMENTO, default='outro')
    data_aquisicao = models.DateField()
    responsavel = models.CharField(max_length = 100, blank=True, null=True)
    status = models.CharField(max_length = 30, choices=STATUS, default = 'Em uso')
    numero_patrimonio = models.CharField(max_length=9, unique = True)
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao
    