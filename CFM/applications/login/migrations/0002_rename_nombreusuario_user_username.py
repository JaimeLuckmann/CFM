# Generated by Django 3.2.9 on 2022-01-04 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='nombreUsuario',
            new_name='username',
        ),
    ]