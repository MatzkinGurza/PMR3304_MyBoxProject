# Generated by Django 5.1.2 on 2024-12-01 14:21

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rating'),
        ('store', '0002_remove_box_image_box_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='ip',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='rating',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='box',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.box'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.FloatField(),
        ),
    ]