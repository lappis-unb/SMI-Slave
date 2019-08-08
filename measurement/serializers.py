from rest_framework import serializers

from .models import MinutelyMeasurement
from .models import QuarterlyMeasurement
from .models import MonthlyMeasurement


class MinutelyMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinutelyMeasurement
        fields = ('id',
                  'transductor',
                  'collection_date',
                  'frequency_a',
                  'voltage_a',
                  'voltage_b',
                  'voltage_c',
                  'current_a',
                  'current_b',
                  'current_c',
                  'active_power_a',
                  'active_power_b',
                  'active_power_c',
                  'total_active_power',
                  'reactive_power_a',
                  'reactive_power_b',
                  'reactive_power_c',
                  'total_reactive_power',
                  'apparent_power_a',
                  'apparent_power_b',
                  'apparent_power_c',
                  'total_apparent_power',
                  'power_factor_a',
                  'power_factor_b',
                  'power_factor_c',
                  'total_power_factor',
                  'dht_voltage_a',
                  'dht_voltage_b',
                  'dht_voltage_c',
                  'dht_current_a',
                  'dht_current_b',
                  'dht_current_c',
                  'transductor',
                  'url')


class MinutelyVoltageThreePhase(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinutelyMeasurement
        fields = ('id',
                  'transductor',
                  'collection_date',
                  'voltage_a',
                  'voltage_b',
                  'voltage_c')


class MinutelyCurrentThreePhase(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinutelyMeasurement
        fields = ('id',
                  'transductor',
                  'collection_date',
                  'current_a',
                  'current_b',
                  'current_c')


class MinutelyActivePowerThreePhase(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinutelyMeasurement
        fields = ('id',
                  'transductor',
                  'collection_date',
                  'active_power_a',
                  'active_power_b',
                  'active_power_c')


class MinutelyReactivePowerThreePhase(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinutelyMeasurement
        fields = ('id',
                  'transductor',
                  'collection_date',
                  'reactive_power_a',
                  'reactive_power_b',
                  'reactive_power_c')


class MinutelyApparentPowerThreePhase(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinutelyMeasurement
        fields = ('id',
                  'transductor',
                  'collection_date',
                  'apparent_power_a',
                  'apparent_power_b',
                  'apparent_power_c')


class MinutelyPowerFactorThreePhase(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinutelyMeasurement
        fields = ('id',
                  'transductor',
                  'collection_date',
                  'power_factor_a',
                  'power_factor_b',
                  'power_factor_c')


class MinutelyDHTVoltageThreePhase(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinutelyMeasurement
        fields = ('id',
                  'transductor',
                  'collection_date',
                  'dht_voltage_a',
                  'dht_voltage_b',
                  'dht_voltage_c')


class MinutelyDHTCurrentThreePhase(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinutelyMeasurement
        fields = ('id',
                  'transductor',
                  'collection_date',
                  'dht_current_a',
                  'dht_current_b',
                  'dht_current_c')


class MinutelyFrequency(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinutelyMeasurement
        fields = ('id',
                  'transductor',
                  'collection_date',
                  'frequency_a')


class MinutelyTotalActivePower(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinutelyMeasurement
        fields = ('id',
                  'transductor',
                  'collection_date',
                  'total_active_power')


class MinutelyTotalReactivePower(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinutelyMeasurement
        fields = ('id',
                  'transductor',
                  'collection_date',
                  'total_reactive_power')


class MinutelyTotalApparentPower(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinutelyMeasurement
        fields = ('id',
                  'transductor',
                  'collection_date',
                  'total_apparent_power')


class MinutelyTotalPowerFactor(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinutelyMeasurement
        fields = ('id',
                  'transductor',
                  'collection_date',
                  'total_power_factor')


class QuarterlyMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuarterlyMeasurement
        fields = ('id',
                  'collection_date',
                  'generated_energy_peak_time',
                  'generated_energy_off_peak_time',
                  'consumption_peak_time',
                  'consumption_off_peak_time',
                  'inductive_power_peak_time',
                  'inductive_power_off_peak_time',
                  'capacitive_power_peak_time',
                  'capacitive_power_off_peak_time',
                  'transductor',
                  'url')


class MonthlyMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MonthlyMeasurement
        fields = ('id',
                  'collection_date',
                  'generated_energy_peak_time',
                  'generated_energy_off_peak_time',
                  'consumption_peak_time',
                  'consumption_off_peak_time',
                  'inductive_power_peak_time',
                  'inductive_power_off_peak_time',
                  'capacitive_power_peak_time',
                  'capacitive_power_off_peak_time',
                  'active_max_power_peak_time',
                  'active_max_power_off_peak_time',
                  'reactive_max_power_peak_time',
                  'reactive_max_power_off_peak_time',
                  'active_max_power_list_peak_time',
                  'active_max_power_list_off_peak_time',
                  'reactive_max_power_list_peak_time',
                  'reactive_max_power_list_off_peak_time',
                  'transductor',
                  'url')
