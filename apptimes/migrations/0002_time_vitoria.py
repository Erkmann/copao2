# Generated by Django 2.1.7 on 2019-03-14 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptimes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='vitoria',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
