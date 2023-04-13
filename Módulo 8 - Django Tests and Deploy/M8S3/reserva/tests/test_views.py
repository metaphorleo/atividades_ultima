import pytest
from datetime import date, timedelta
from reserva.models import Reserva

@pytest.fixture
def dados_validos():
    amanha = date.today() + timedelta(days = 1)
    dados = {
        'nome': 'João',
        'email': 'joao@email.com',
        'nome_pet': 'Tom',
        'tamanho': 0,
        'dia_reserva': amanha,
        'turno': 'tarde',
        'observacoes': 'O Tom está bem fedorento.'
    }
    return dados

@pytest.mark.django_db
def test_reserva_view_deve_retornar_sucesso(client, dados_validos):
    response = client.post('/reserva/criar/', dados_validos)

    assert response.status_code == 200
    assert 'Reserva realizada com sucesso, em breve iremos entrar em contato!' in str(response.content)

@pytest.mark.django_db
def test_reserva_view_deve_criar_reserva(client, dados_validos):
    client.post('/reserva/criar/', dados_validos)

    assert Reserva.objects.all().count() == 1
    reserva = Reserva.objects.first()

    assert reserva.nome == dados_validos['nome']
    assert reserva.nome_pet == dados_validos['nome_pet']