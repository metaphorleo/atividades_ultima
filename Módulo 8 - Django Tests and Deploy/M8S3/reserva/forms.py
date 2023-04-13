from django import forms
from reserva.models import Reserva
from datetime import date

class ReservaForm(forms.ModelForm):
    def clean_dia_reserva(self):
        dia_reserva = self.cleaned_data['dia_reserva']
        hoje = date.today()
        if dia_reserva < hoje:
            raise forms.ValidationError('Data inválida, não é possível realizar uma reserva para o passado.')
        if Reserva.objects.filter(dia_reserva=dia_reserva).count() >= 4:
            raise forms.ValidationError('Agenda para data lotada, selecione outro dia.')
        return dia_reserva

    class Meta:
        model = Reserva
        fields = [
            'nome', 'email', 'nome_pet', 'tamanho', 'telefone', 'dia_reserva', 'turno',
            'observacoes'
        ]