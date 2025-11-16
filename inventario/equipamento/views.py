from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Equipamento
from .forms import EquipamentoForm

def listar_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'equipamento/listar_equipamentos.html', {'equipamentos': equipamentos})

# CADASTRO DE EQUIPAMENTOS

def cadastrar_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipamento:listar_equipamentos') #! Checar singular
    else:
        form = EquipamentoForm()
    return render(request, 'equipamento/form_equipamentos.html', {'form': form})

# EDIÇÃO DE EQUIPAMENTOS

def editar_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamento, id = equipamento_id)

    if request.method == 'POST':
        form = EquipamentoForm(request.POST, isinstance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('equipamento:listar_equipamentos')
        else:
            # Se for GET, mostra o form já preenchido
            form = EquipamentoForm(isinstance=Equipamento)

        return render(request, 'equipamento/editar_equipamento.html', {'form': form})
    
# EXCLUSÃO DE EQUIPAMENTOS    

class ExcluirEquipamentoView(DeleteView):
    model = Equipamento 
    template_name = 'equipamento/excluir_equipamento.html'
    success_url = reverse_lazy('equipamento:listar_equipamentos')

    def delete(self, request, *args, **kwargs):
        equipamento = self.get_object()

        # Informações que serão utilizadas na mensagem
        descricao = equipamento.descricao
        patrimonio = equipamento.patrimonio
        # nome = equipamento.nome
        
        messages.success(request, 
                         f'O equipamento {equipamento.nome}, patrimônio número {equipamento.patrimonio}, foi excluído com sucesso.'
                         )
        return super().delete(request, *args, **kwargs)