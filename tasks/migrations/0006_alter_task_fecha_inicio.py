# Generated by Django 4.2 on 2023-05-02 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_fecha_finalizacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Fecha_Inicio',
            field=models.DateTimeField(null=True),
        ),
    ]
