# Generated by Django 4.2.13 on 2024-06-29 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_fisico_quimicos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='alcalinidade_bicarbonato',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='alcalinidade_carbonato',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='alcalinidade_hidroxidos',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='alcalinidade_total',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='aluminio',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='cloreto',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='condutividade_eletrica_25',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='cor_aparente',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='cor_verdadeira',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='dureza_calcio',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='dureza_magnesio',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='dureza_total',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='estimativa_tds',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='ferro_total',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='fluoreto',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='manganes',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='nitrato',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='nitrito',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='oxigenio_dissolvido',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='potassio',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='silica',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='sodio',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='solidos_totais',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='sulfatos',
        ),
        migrations.RemoveField(
            model_name='fisicoquimico',
            name='turbidez',
        ),
        migrations.AlterField(
            model_name='fisicoquimico',
            name='cloro_residual_livre',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='fisicoquimico',
            name='ph',
            field=models.IntegerField(null=True),
        ),
    ]
