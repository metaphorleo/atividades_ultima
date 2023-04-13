import pytest
import datetime
from model_bakery import baker
from reserva.models import Petshop
from rest_api.serializers import AgendamentoModelSerializer

@pytest.fixture
def dados_agendamento_errado():
    ontem = datetime.date.today() - datetime.timedelta(days = 1)
    petshop = baker.make(Petshop)
    return {
        'nome': 'nome teste',
        'email': 'email@email.com',
        'nome_pet': 'pet teste',
        'tamanho': 0,
        'dia_reserva': ontem,
        'turno': 'manhã',
        'observacoes': '',
        'petshop': petshop.pk
    }

@pytest.mark.django_db
def test_data_agendamento_invalida(dados_agendamento_errado):
    serializer = AgendamentoModelSerializer(data = dados_agendamento_errado)

    assert not serializer.is_valid()