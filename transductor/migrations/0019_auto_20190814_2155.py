# Generated by Django 2.1.5 on 2019-08-14 21:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transductor', '0018_auto_20190814_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energytransductor',
            name='installation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 15, 0, 55, 23, 882966, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='energytransductor',
            name='last_clock_battery_change',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 15, 0, 55, 23, 883060, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='energytransductor',
            name='last_collection',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 15, 0, 55, 23, 882869, tzinfo=utc)),
        ),
    ]