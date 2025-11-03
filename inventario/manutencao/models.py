from django.db import models
from inventario.equipamento.models import Equipamento
# Manutenção
class Manutencao(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, related_name='manutencoes')
    data = models.DateField()
    tecnico = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return f"Manutenção de {self.equipamento.descricao} em {self.data}"