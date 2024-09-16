# Generated by Django 5.1.1 on 2024-09-16 00:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='administrador',
            options={'verbose_name_plural': 'Administradores'},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AddField(
            model_name='administrador',
            name='user_admin',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
