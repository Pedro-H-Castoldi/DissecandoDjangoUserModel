# Generated by Django 3.0.6 on 2020-05-17 21:48

from django.db import migrations
import usuarios.models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', usuarios.models.UsuarioManager()),
            ],
        ),
    ]
