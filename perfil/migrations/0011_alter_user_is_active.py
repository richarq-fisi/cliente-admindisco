# Generated by Django 5.1.1 on 2024-09-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0010_departamento_distrito_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
