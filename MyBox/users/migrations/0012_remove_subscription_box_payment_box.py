# Generated by Django 5.1.3 on 2024-11-29 00:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_payment_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='box',
        ),
        migrations.AddField(
            model_name='payment',
            name='box',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='users.cartitem'),
            preserve_default=False,
        ),
    ]