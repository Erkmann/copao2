# Generated by Django 2.1.7 on 2019-03-21 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptimes', '0005_auto_20190321_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='rodada',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
