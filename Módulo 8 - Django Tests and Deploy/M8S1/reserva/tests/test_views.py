from pytest_django.asserts import assertTemplateUsed
from datetime import date, timedelta

def test_reserva_view_deve_retornar_template(client):
    response = client.get('/reserva/criar/')

    assert response.status_code == 200
    assertTemplateUsed(response, 'reserva.html')