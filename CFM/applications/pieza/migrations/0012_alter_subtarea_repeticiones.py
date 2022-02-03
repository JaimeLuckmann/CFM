# Generated by Django 3.2.9 on 2022-01-24 22:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieza', '0011_alter_subtarea_repeticiones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtarea',
            name='repeticiones',
            field=models.DecimalField(decimal_places=5, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]
