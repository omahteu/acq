# Generated by Django 4.2.13 on 2024-06-25 10:49

import apps.autenticacao.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('apps_usuarios', '0001_initial'),
        ('apps_hidricos', '0001_initial'),
        ('apps_clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.CharField(max_length=50, unique=True)),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')),
                ('active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('bacia_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_hidricos.hidricos')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_clientes.cliente')),
                ('groups', models.ManyToManyField(related_name='custom_users', to='auth.group')),
                ('perfis', models.ManyToManyField(to='apps_usuarios.perfil')),
                ('user_permissions', models.ManyToManyField(related_name='custom_users', to='auth.permission')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', apps.autenticacao.models.UserManager()),
            ],
        ),
    ]
