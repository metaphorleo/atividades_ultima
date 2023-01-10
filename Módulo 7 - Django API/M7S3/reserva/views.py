from django.shortcuts import render
from reserva.forms import ReservaForm

def reserva(request):
    form = ReservaForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    else:
        sucesso = False
    contexto = {
        'form': form,
        'sucesso': sucesso,
    }
    return render(request, 'reserva.html', contexto)