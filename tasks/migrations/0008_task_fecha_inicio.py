# Generated by Django 4.2 on 2023-05-02 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_remove_task_fecha_inicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Fecha_Inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]