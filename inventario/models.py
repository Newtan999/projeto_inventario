from django.db import models

# Setor
class Setor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        # Aprimorar mensagem
        return self.nome