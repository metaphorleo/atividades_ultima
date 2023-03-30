from datetime import date
import pytest
from model_bakery import baker
from reserva.models import Reserva

@pytest.fixture
def reserva():
    data = date(2023, 8, 30)
    reserva = baker.make(
        Reserva,
        nome = 'Tom',
        dia_reserva = data,
        turno='tarde'
    )
    return reserva

@pytest.mark.django_db
def test_str_reserva_deve_retornar_string_formatada(reserva):
    assert str(reserva) == 'Tom: 2023-08-30 - tarde'