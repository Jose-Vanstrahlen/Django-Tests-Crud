# Generated by Django 4.2 on 2023-05-02 19:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_fecha_finalizacion_task_fecha_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Fecha_Finalizacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='Fecha_Inicio',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 19, 38, 40, 319407, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
