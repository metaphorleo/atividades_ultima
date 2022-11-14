from django.contrib import admin
from reserva.models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'nome_pet', 'telefone', 'dia_reserva', 'turno']
    search_fields = ['nome', 'email', 'nome_pet', 'telefone']
    list_display = ['dia_reserva', 'turno', 'tamanho']

