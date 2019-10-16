from rest_framework import serializers
import django.utils.timezone
from datetime import datetime

from .models import EnergyTransductor


class EnergyTransductorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EnergyTransductor
        fields = (
            'serial_number',
            'ip_address',
            'physical_location',
            'geolocation_latitude',
            'geolocation_longitude',
            'broken',
            'active',
            'firmware_version',
            'installation_date',
            'last_collection',
            'last_clock_battery_change',
            'model',
            'url',
        )

    def create(self, validated_data):
        transductor = EnergyTransductor.objects.create(**validated_data)
        transductor.installation_date = django.utils.timezone.now()
        transductor.last_collection = datetime(1970, 1, 1, 0, 0, 0)
        transductor.last_clock_battery_change = django.utils.timezone.now()
        transductor.save()
        return transductor


class ActiveTransductorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EnergyTransductor
        fields = (
            'serial_number',
            'active',
        )


class BrokenTransductorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EnergyTransductor
        fields = (
            'serial_number',
            'broken',
        )
