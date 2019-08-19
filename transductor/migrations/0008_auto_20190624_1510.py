# Generated by Django 2.1.5 on 2019-06-24 15:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transductor', '0007_auto_20190624_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energytransductor',
            name='installation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 24, 18, 10, 40, 318890, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='energytransductor',
            name='last_clock_battery_change',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 24, 18, 10, 40, 318986, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='energytransductor',
            name='last_collection',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 24, 18, 10, 40, 318793, tzinfo=utc)),
        ),
    ]