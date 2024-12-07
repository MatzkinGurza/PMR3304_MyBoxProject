# Generated by Django 5.1.2 on 2024-12-01 23:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_payment_box'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='background_url',
        ),
        migrations.AlterField(
            model_name='payment',
            name='CPF_do_titular',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='payment',
            name='PIN',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='payment',
            name='nome_no_cartão',
            field=models.CharField(default='não informado', max_length=255),
        ),
        migrations.AlterField(
            model_name='payment',
            name='número_do_cartão',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='payment',
            name='validade',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='CEP',
            field=models.CharField(default='00000-000', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='CPF',
            field=models.CharField(default='000.000.000-00', max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='endereço',
            field=models.TextField(default='Endereço não informado', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nascimento',
            field=models.DateTimeField(default='2000-01-01', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telefone',
            field=models.CharField(default='(00) 00000-0000', max_length=15, null=True),
        ),
    ]