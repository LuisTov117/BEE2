# Generated by Django 4.2.3 on 2023-07-21 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BEV2', '0003_alumnos_carrera'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='justificacion',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='objetivo',
            field=models.CharField(default='', max_length=300),
        ),
    ]
