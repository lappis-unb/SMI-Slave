# Generated by Django 2.1.5 on 2019-08-14 21:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transductor', '0017_auto_20190814_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energytransductor',
            name='installation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 15, 0, 47, 27, 199323, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='energytransductor',
            name='last_clock_battery_change',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 15, 0, 47, 27, 199416, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='energytransductor',
            name='last_collection',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 15, 0, 47, 27, 199228, tzinfo=utc)),
        ),
    ]