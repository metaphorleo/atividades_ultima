import pytest
import datetime
from rest_framework.test import APIClient
from model_bakery import baker
from reserva.models import Petshop, Reserva
from rest_api.serializers import PetshopModelSerializer

@pytest.fixture
def dados_agendamento():
    hoje = datetime.date.today()
    petshop = baker.make(Petshop)
    return {
        'nome': 'nome teste',
        'email': 'email@email.com',
        'nome_pet': 'pet teste',
        'tamanho': 0,
        'dia_reserva': hoje,
        'turno': 'manhã',
        'observacoes': '',
        'petshop': petshop.pk
    }

@pytest.fixture
def usuario():
    return baker.make('auth.User')

@pytest.mark.django_db
def test_criar_agendamento(usuario, dados_agendamento):
    cliente = APIClient()
    cliente.force_authenticate(usuario)
    resposta = cliente.post('/api/agendamento', dados_agendamento)
    assert resposta.status_code == 201

@pytest.mark.django_db
def test_todos_petshops():
    cliente = APIClient()
    resposta = cliente.get('/api/petshop')
    
    assert len(resposta.data['results']) == 0