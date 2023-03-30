# Generated by Django 4.1.2 on 2022-11-14 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={'ordering': ['-data'], 'verbose_name': 'Formulário de Contato', 'verbose_name_plural': 'Formulários de Contatos'},
        ),
        migrations.AddField(
            model_name='contato',
            name='lido',
            field=models.BooleanField(blank=True, default=False, verbose_name='Lido'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='data',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data Envio'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.EmailField(max_length=75, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='mensagem',
            field=models.TextField(verbose_name='Mensagem'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
    ]
