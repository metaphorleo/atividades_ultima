# Generated by Django 4.1.5 on 2023-03-28 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0003_alter_reserva_observacoes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Petshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Petshop')),
                ('rua', models.CharField(max_length=50, verbose_name='Endereço')),
                ('numero', models.CharField(max_length=50, verbose_name='Número')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
            ],
        ),
        migrations.AddField(
            model_name='reserva',
            name='petshop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='reserva.petshop'),
        ),
    ]
