# Generated by Django 4.2 on 2023-04-28 21:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_task_fecha_finalizacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Fecha_Creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]