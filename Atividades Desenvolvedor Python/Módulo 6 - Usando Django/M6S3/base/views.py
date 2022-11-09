from django.shortcuts import render
from base.forms import ContatoForm, ReservaForm

def inicial(request):
    return render(request, 'inicial.html')

def contato(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    else:
        sucesso = False
    contexto = {
        'telefone': '(99) 99999-9999',
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'contato.html', contexto)

def reserva(request):
    form = ReservaForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    else:
        sucesso = False
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'reserva.html', contexto)