from django.shortcuts import render

# Create your views here.
def inicial(request):
    return render(request, 'inicial.html')

def contato(request):
    contexto = {
        'telefone': '(99) 99999-9999'
    }
    return render(request, 'contato.html', contexto)