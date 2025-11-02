from django.db import models

# Setor
class Setor(models.Model):
    nome = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome

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
    
# Manutenção
class Manutencao(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, related_name='manutencoes')
    data = models.DateField()
    tecnico = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return f"Manutenção de {self.equipamento.descricao} em {self.data}"