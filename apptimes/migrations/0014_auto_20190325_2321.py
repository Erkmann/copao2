# Generated by Django 2.1.7 on 2019-03-25 23:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptimes', '0013_auto_20190325_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferencia',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 25, 23, 21, 26, 990319)),
        ),
    ]
