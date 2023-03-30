# Generated by Django 4.1.2 on 2022-11-08 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('mensagem', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
