# Generated by Django 2.1.7 on 2019-03-22 14:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apptimes', '0008_auto_20190322_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferencia',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 22, 14, 31, 19, 807443)),
        ),
        migrations.AlterField(
            model_name='transferencia',
            name='time_vendedor',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='vendedor', to='apptimes.Time'),
        ),
    ]
