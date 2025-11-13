from django.db import models

# Setor
class Setor(models.Model):

    STATUS =  [
        ('ativo', 'inativo'),

    ]

    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)
    

    def __str__(self):
        return f"Setor {self.descricao}, responsável {self.responsavel}."