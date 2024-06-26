# Generated by Django 4.2.13 on 2024-06-25 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apps_hidricos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hidrometrico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pressao', models.FloatField()),
                ('nivel_agua', models.FloatField()),
                ('vazao', models.FloatField()),
                ('consumo', models.FloatField()),
                ('bacia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_hidricos.hidricos')),
            ],
        ),
    ]
