# Generated by Django 5.1.1 on 2024-09-17 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_rename_user_admin_administrador_nombre_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrador',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
