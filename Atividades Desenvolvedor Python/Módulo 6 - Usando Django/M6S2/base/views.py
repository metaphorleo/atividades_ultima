from django.shortcuts import render

# Create your views here.
def inicial(request):
    return render(request, 'inicial.html')

def contato(request):
    return render(request, 'contato.html')