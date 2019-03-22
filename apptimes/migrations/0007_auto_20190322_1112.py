# Generated by Django 2.1.7 on 2019-03-22 11:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apptimes', '0006_partida_rodada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(default=datetime.datetime(2019, 3, 22, 11, 12, 38, 821329))),
            ],
        ),
        migrations.AddField(
            model_name='time',
            name='admin_time',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apptimes.Usuario'),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='id_time',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apptimes.Time'),
        ),
        migrations.AddField(
            model_name='transferencia',
            name='jogador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apptimes.Jogador'),
        ),
        migrations.AddField(
            model_name='transferencia',
            name='time_comprador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comprador', to='apptimes.Time'),
        ),
        migrations.AddField(
            model_name='transferencia',
            name='time_vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='vendedor', to='apptimes.Time'),
        ),
    ]
