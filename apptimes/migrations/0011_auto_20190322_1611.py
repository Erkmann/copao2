# Generated by Django 2.1.7 on 2019-03-22 16:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apptimes', '0010_auto_20190322_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransferenciaJogador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jogador', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apptimes.Jogador')),
            ],
        ),
        migrations.RemoveField(
            model_name='transferencia',
            name='jogador',
        ),
        migrations.AlterField(
            model_name='transferencia',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 22, 16, 11, 19, 149622)),
        ),
        migrations.AddField(
            model_name='transferenciajogador',
            name='transferencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apptimes.Transferencia'),
        ),
    ]
