from django import forms
from base.models import Contato, Reserva
class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ["nome", "email", "mensagem"]

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["nomedopet", "telefone", "diareserva", "observacoes"]