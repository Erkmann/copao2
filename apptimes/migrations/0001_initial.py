# Generated by Django 2.1.7 on 2019-03-21 17:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curtir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_camisa', models.IntegerField(default=0)),
                ('nome', models.CharField(max_length=45)),
                ('gols', models.IntegerField(default=0)),
                ('cartao_amarelo', models.IntegerField(default=0)),
                ('cartao_vermelho', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=datetime.date.today)),
                ('gols_timeA', models.IntegerField(default=0, null=True)),
                ('gols_timeB', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(max_length=55)),
                ('nome_time', models.CharField(max_length=55)),
                ('pontos', models.IntegerField()),
                ('cor', models.CharField(max_length=30)),
                ('saldo_gols', models.IntegerField()),
                ('vitoria', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=35)),
            ],
        ),
        migrations.AddField(
            model_name='partida',
            name='id_time_mandante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mandante', to='apptimes.Time'),
        ),
        migrations.AddField(
            model_name='partida',
            name='id_time_visitante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='visitante', to='apptimes.Time'),
        ),
        migrations.AddField(
            model_name='jogador',
            name='id_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apptimes.Time'),
        ),
        migrations.AddField(
            model_name='curtir',
            name='time_id_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apptimes.Time'),
        ),
        migrations.AddField(
            model_name='curtir',
            name='usuario_id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apptimes.Usuario'),
        ),
    ]
