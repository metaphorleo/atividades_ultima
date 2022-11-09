from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

class Reserva(models.Model):
    nomedopet = models.CharField("Nome do Pet", max_length=50)
    telefone = models.CharField("Telefone para contato", max_length=20)
    diareserva = models.DateField("Dia da reserva")
    observacoes = models.TextField("Observações", blank=True)
