# Generated by Django 2.1.7 on 2019-03-14 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(max_length=55)),
                ('nome_time', models.CharField(max_length=55)),
                ('pontos', models.IntegerField()),
                ('cor', models.CharField(max_length=30)),
                ('saldo_gols', models.IntegerField()),
            ],
        ),
    ]
