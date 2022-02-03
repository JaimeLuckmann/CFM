# Generated by Django 3.2.9 on 2022-01-09 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pieza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='filaCarrito',
            fields=[
                ('id_fila', models.BigAutoField(primary_key=True, serialize=False)),
                ('costoTarea', models.PositiveIntegerField(verbose_name='Costo Tarea')),
                ('Tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pieza.tarea')),
            ],
        ),
    ]
