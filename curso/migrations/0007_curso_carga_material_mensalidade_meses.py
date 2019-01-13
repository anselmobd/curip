# Generated by Django 2.1.4 on 2019-01-13 13:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0006_trilha_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='carga',
            field=models.PositiveIntegerField(default=0, verbose_name='carga horária'),
        ),
        migrations.AddField(
            model_name='curso',
            name='material',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Material Didádico'),
        ),
        migrations.AddField(
            model_name='curso',
            name='mensalidade',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='curso',
            name='meses',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Duração (meses)'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trilha',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]