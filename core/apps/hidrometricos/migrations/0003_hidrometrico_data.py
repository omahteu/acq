# Generated by Django 4.2.13 on 2024-08-04 20:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apps_hidrometricos', '0002_remove_hidrometrico_consumo'),
    ]

    operations = [
        migrations.AddField(
            model_name='hidrometrico',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
