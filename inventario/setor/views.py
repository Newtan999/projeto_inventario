from django.shortcuts import render, redirect, get_object_or_404
from .models import Setor
from .forms import SetorForm
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib import messages


# Listar
def listar_setores(request):
    setores = Setor.objects.all()
    return render(request, 'setor/listar_setores.html', {'setores': setores})

# Cadastrar
def cadastrar_setor(request):
    if request.method == 'POST':
        form = SetorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('setor:listar_setores')
    else:
        form = SetorForm()
    return render(request, 'setor/form_setores.html', {'form': form})

#Ediitar
def editar_setor(request, pk):
    setor = get_object_or_404(Setor, id=pk)

    if request.method == 'POST':
        form = SetorForm(request.POST, instance=setor)
        if form.is_valid():
            form.save()
            return redirect('setor:listar_setores')
    else:
        form = SetorForm(instance=setor)

    return render(request, 'setor/editar_setor.html', {'form': form, 'setor': setor})

        
#Excluir
class ExcluirSetorView(DeleteView):
    model = Setor
    template_name = 'setor/excluir_setor.html'
    success_url = reverse_lazy('setor:listar_setores')
    
    def delete(self, request, *args, **kwargs):
        setor = self.get_object()
        nome = setor.nome
        messages.success(request, f'O setor {nome} foi excluído com sucesso.')
        return super().delete(request, *args, **kwargs)