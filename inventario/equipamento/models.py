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


    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length = 100)
    tipo = models.CharField(max_length=20, choices=TIPO_EQUIPAMENTO, default='outro')
    data_aquisicao = models.DateField()
    # Responsável vem do cadastro de setor
    responsavel = models.ForeignKey(Setor, on_delete=models.PROTECT)
    status = models.CharField(max_length = 30, choices=STATUS, default = 'Em uso')
    numero_patrimonio = models.CharField(max_length=9, unique = True)
    # Setor vem do cadastro de setor
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)

    def __str__(self):
        return {self.descricao}

    '''def save(self, *args, **kwargs):
        if not self.numero_patrimonio:
            ultimo = Equipamento.objects.order_by('-id').first()
            if ultimo and ultimo.numero_patrimonio and ultimo.numero_patrimonio.isdigit():
                novo_numero = int(ultimo.numero_patrimonio) + 1
            else:
                novo_numero = 1
            
            self.numero_patrimonio = f"{novo_numero:09d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.descricao} ({self.numero_patrimonio})"'''