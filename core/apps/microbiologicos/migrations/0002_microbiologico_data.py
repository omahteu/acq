# Generated by Django 4.2.13 on 2024-08-04 20:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apps_microbiologicos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='microbiologico',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
