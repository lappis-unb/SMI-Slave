# Generated by Django 2.1.5 on 2019-09-24 11:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyTransductor',
            fields=[
                ('serial_number', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('ip_address', models.CharField(default='0.0.0.0', max_length=15, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_ip_address', message='Incorrect IP address format', regex='^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}$')])),
                ('model', models.CharField(default='EnergyTransductorModel', max_length=50)),
                ('last_collection', models.DateTimeField(blank=True, null=True)),
                ('broken', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('firmware_version', models.CharField(max_length=20)),
                ('installation_date', models.DateTimeField(blank=True, null=True)),
                ('physical_location', models.CharField(default='', max_length=30)),
                ('geolocation_longitude', models.DecimalField(decimal_places=10, max_digits=15)),
                ('geolocation_latitude', models.DecimalField(decimal_places=10, max_digits=15)),
                ('last_clock_battery_change', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
