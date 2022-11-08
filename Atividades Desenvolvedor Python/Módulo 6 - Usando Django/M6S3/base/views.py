from django.shortcuts import render
from base.forms import ContatoForm
# Create your views here.
def inicial(request):
    return render(request, 'inicial.html')

def contato(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        sucesso = True
    else:
        sucesso = False
    contexto = {
        'telefone': '(99) 99999-9999',
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'contato.html', contexto)