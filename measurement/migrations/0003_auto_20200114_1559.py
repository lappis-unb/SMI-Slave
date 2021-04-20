# Generated by Django 2.1.5 on 2020-01-14 15:59

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_auto_20200114_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlymeasurement',
            name='active_max_power_list_off_peak',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=None, size=None),
        ),
        migrations.AddField(
            model_name='monthlymeasurement',
            name='active_max_power_list_off_peak_time',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), default=None, size=None),
        ),
        migrations.AddField(
            model_name='monthlymeasurement',
            name='active_max_power_list_peak',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=None, size=None),
        ),
        migrations.AddField(
            model_name='monthlymeasurement',
            name='active_max_power_list_peak_time',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), default=None, size=None),
        ),
        migrations.AddField(
            model_name='monthlymeasurement',
            name='reactive_max_power_list_off_peak',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=None, size=None),
        ),
        migrations.AddField(
            model_name='monthlymeasurement',
            name='reactive_max_power_list_off_peak_time',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), default=None, size=None),
        ),
        migrations.AddField(
            model_name='monthlymeasurement',
            name='reactive_max_power_list_peak',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=None, size=None),
        ),
        migrations.AddField(
            model_name='monthlymeasurement',
            name='reactive_max_power_list_peak_time',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), default=None, size=None),
        ),
    ]