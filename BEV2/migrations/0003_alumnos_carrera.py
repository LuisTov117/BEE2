# Generated by Django 4.2.3 on 2023-07-18 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BEV2', '0002_alumnos_password_empresa_passworde'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='carrera',
            field=models.CharField(default='', max_length=80),
        ),
    ]