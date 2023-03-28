from django.contrib import admin
from reserva.models import Reserva, Petshop

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'nome_pet', 'telefone', 'dia_reserva', 'turno', 'petshop_nome']
    search_fields = ['nome', 'nome_pet', 'dia_reserva', 'petshop__nome']

    def petshop_nome(self, obj):
        return obj.petshop.nome

    petshop_nome.short_description = 'Petshop'


@admin.register(Petshop)
class PetshopAdmin(admin.ModelAdmin):
    list_display = ['nome', 'rua', 'numero', 'bairro']
    search_fields = ['nome', 'rua', 'bairro']

