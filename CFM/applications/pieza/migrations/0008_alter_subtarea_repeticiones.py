# Generated by Django 3.2.9 on 2022-01-24 22:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieza', '0007_alter_subtarea_repeticiones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtarea',
            name='repeticiones',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]
