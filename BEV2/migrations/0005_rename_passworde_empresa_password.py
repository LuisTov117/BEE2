# Generated by Django 4.2.3 on 2023-07-21 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BEV2', '0004_proyecto_justificacion_proyecto_objetivo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='passwordE',
            new_name='password',
        ),
    ]
