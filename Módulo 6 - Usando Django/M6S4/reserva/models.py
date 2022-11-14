from django.db import models

class Reserva(models.Model):
    TAMANHO_OPCOES = (
        (0, 'Pequeno'),
        (1, 'Médio'),
        (2, 'Grande'),
    )
    TURNO_OPCOES = (
        ('manhã', 'Manhã'),
        ('tarde', 'Tarde'),
    )
    nome = models.CharField(verbose_name='Nome', max_length=50)
    email = models.EmailField(verbose_name='E-mail')
    nome_pet = models.CharField(verbose_name="Nome do Pet", max_length=50)
    telefone = models.CharField(verbose_name="Telefone para contato", max_length=11, blank=True)
    dia_reserva = models.DateField(verbose_name="Dia da reserva", help_text='dd/mm/aaaa')
    turno = models.CharField(verbose_name='Turno', max_length=10, choices=TURNO_OPCOES)
    tamanho = models.IntegerField(verbose_name='Tamanho', choices=TAMANHO_OPCOES)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.nome}: {self.dia_reserva} - {self.turno}'

    class Meta:
        verbose_name = 'Reserva de Banho'
        verbose_name_plural = 'Reservas de Banho'