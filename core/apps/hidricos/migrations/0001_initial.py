# Generated by Django 4.2.13 on 2024-06-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hidricos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.BooleanField(null=True)),
            ],
        ),
    ]
