from django.db import models
from datetime import datetime
from transductor.models import EnergyTransductor
from django.contrib.postgres.fields import ArrayField, HStoreField
from boogie.rest import rest_api
import json
from django.core import serializers


class Measurement(models.Model):
    """
    Abstract class responsible to create a base for measurements and optimize
    performance from queries.

    Attributes:
        collection_date (datetime): The exactly collection time.

    """
    collection_date = models.DateTimeField(default=datetime.now)

    class Meta:
        abstract = True

    def save_measurements(self, values_list):
        """
        Method responsible to save measurements based on values list received.

        Args:
            values_list (list): The list with all important
            measurements values.

        Returns:
            None
        """
        raise NotImplementedError


@rest_api()
class EnergyMeasurement(Measurement):
    """
    Class responsible to store energy measurements,
    considering a three-phase energy system.

    Attributes:
        transductor (EnergyTransductor): The transductor which conducted
        measurements.

        consumption_a (float): The total consumption on phase A.
        (since last reset)
        consumption_b (float): The total consumption on phase B.
        (since last reset)
        consumption_c (float): The total consumption on phase C.
        (since last reset)
        total_consumption (float): The total consumption of transductor.
        (since last reset)
    """
    transductor = models.ForeignKey(
        EnergyTransductor, related_name="measurements", on_delete=models.CASCADE
    )

    def __str__(self):
        return '%s' % self.collection_date

    def get_minutely_measurements(self):
        all_measurements = MinutelyMeasurement.objects.all()
        serialized_measurements = []
        for measurement in all_measurements:
            serialized_measurements.append(
                json.loads(serializers.serialize('json', [measurement]))
            )

        return serialized_measurements

    def get_quartely_measurements(self):
        all_measurements = QuarterlyMeasurement.objects.all()
        serialized_measurements = []
        for measurement in all_measurements:
            serialized_measurements.append(
                json.loads(serializers.serialize('json', [measurement]))
            )

        return serialized_measurements

    def get_monthly_measurements(self):
        all_measurements = MonthlyMeasurement.objects.all()
        serialized_measurements = []
        for measurement in all_measurements:
            values = json.loads(serializers.serialize('json', [measurement]))

            methods_names = [
                'active_max_power_list_peak_time', 
                'active_max_power_list_off_peak_time',
                'reactive_max_power_list_peak_time', 
                'reactive_max_power_list_off_peak_time'
            ]

            for method_name in methods_names:
                max_power_attr = getattr(measurement, method_name)
                correct_max_power_list = self.get_correct_max_power_list(
                    measurement, max_power_attr
                )
                self.set_correct_value_to_max_power_list(
                    correct_max_power_list, method_name, values
                )

            serialized_measurements.append(values)
        return serialized_measurements

    def get_correct_max_power_list(self, measurement, max_power_list):
        correct_max_power_list = max_power_list
        for values in correct_max_power_list:
            if len(values) == 2:
                values['value'] = json.loads(values['value'])
                values['date'] = json.loads(values['date'])
            else:
                values['value'] = json.loads(values['value'])

        return correct_max_power_list

    def set_correct_value_to_max_power_list(
        self, correct_max_power_list, field_name, values
    ):
        values[0]['fields'][field_name] = correct_max_power_list

    def save_measurements(self, values_list, transductor):
        """
        Method responsible to save measurements based on values
        list received.
        Args:
            values_list (list): The list with all important
                measurements values.
            transductor (Transductor): Related transductor object
        Return:
            None
        """
        raise NotImplementedError


class MinutelyMeasurement(EnergyMeasurement):

    frequency_a = models.FloatField(default=0)

    voltage_a = models.FloatField(default=0)
    voltage_b = models.FloatField(default=0)
    voltage_c = models.FloatField(default=0)

    current_a = models.FloatField(default=0)
    current_b = models.FloatField(default=0)
    current_c = models.FloatField(default=0)

    active_power_a = models.FloatField(default=0)
    active_power_b = models.FloatField(default=0)
    active_power_c = models.FloatField(default=0)
    total_active_power = models.FloatField(default=0)

    reactive_power_a = models.FloatField(default=0)
    reactive_power_b = models.FloatField(default=0)
    reactive_power_c = models.FloatField(default=0)
    total_reactive_power = models.FloatField(default=0)

    apparent_power_a = models.FloatField(default=0)
    apparent_power_b = models.FloatField(default=0)
    apparent_power_c = models.FloatField(default=0)
    total_apparent_power = models.FloatField(default=0)

    power_factor_a = models.FloatField(default=0)
    power_factor_b = models.FloatField(default=0)
    power_factor_c = models.FloatField(default=0)
    total_power_factor = models.FloatField(default=0)

    dht_voltage_a = models.FloatField(default=0)
    dht_voltage_b = models.FloatField(default=0)
    dht_voltage_c = models.FloatField(default=0)

    dht_current_a = models.FloatField(default=0)
    dht_current_b = models.FloatField(default=0)
    dht_current_c = models.FloatField(default=0)

    def save_measurements(values_list, transductor):
        """
        Method responsible to save measurements based on values
        list received.
        Args:
            values_list (list): The list with all important
            measurements values.
        Return:
            None
        """
        minutely_measurement = MinutelyMeasurement()
        minutely_measurement.transductor = transductor

        # saving the datetime from transductor
        minutely_measurement.collection_date = datetime(
            values_list[0],
            values_list[1],
            values_list[2],
            values_list[3],
            values_list[4],
            values_list[5]
        )

        minutely_measurement.frequency_a = values_list[6]
        minutely_measurement.voltage_a = values_list[7]
        minutely_measurement.voltage_b = values_list[8]
        minutely_measurement.voltage_c = values_list[9]
        minutely_measurement.current_a = values_list[10]
        minutely_measurement.current_b = values_list[11]
        minutely_measurement.current_c = values_list[12]
        minutely_measurement.active_power_a = values_list[13]
        minutely_measurement.active_power_b = values_list[14]
        minutely_measurement.active_power_c = values_list[15]
        minutely_measurement.total_active_power = values_list[16]
        minutely_measurement.reactive_power_a = values_list[17]
        minutely_measurement.reactive_power_b = values_list[18]
        minutely_measurement.reactive_power_c = values_list[19]
        minutely_measurement.total_reactive_power = values_list[20]
        minutely_measurement.apparent_power_a = values_list[21]
        minutely_measurement.apparent_power_b = values_list[22]
        minutely_measurement.apparent_power_c = values_list[23]
        minutely_measurement.total_apparent_power = values_list[24]
        minutely_measurement.power_factor_a = values_list[25]
        minutely_measurement.power_factor_b = values_list[26]
        minutely_measurement.power_factor_c = values_list[27]
        minutely_measurement.total_power_factor = values_list[28]
        minutely_measurement.dht_voltage_a = values_list[29]
        minutely_measurement.dht_voltage_b = values_list[30]
        minutely_measurement.dht_voltage_c = values_list[31]
        minutely_measurement.dht_current_a = values_list[32]
        minutely_measurement.dht_current_b = values_list[33]
        minutely_measurement.dht_current_c = values_list[34]
        minutely_measurement.consumption_a = values_list[35]
        minutely_measurement.consumption_b = values_list[36]
        minutely_measurement.consumption_c = values_list[37]
        minutely_measurement.total_consumption = values_list[38]

        minutely_measurement.save()


class QuarterlyMeasurement(EnergyMeasurement):

    generated_energy_peak_time = models.FloatField(default=0)
    generated_energy_off_peak_time = models.FloatField(default=0)
    consumption_peak_time = models.FloatField(default=0)
    consumption_off_peak_time = models.FloatField(default=0)
    inductive_power_peak_time = models.FloatField(default=0)
    inductive_power_off_peak_time = models.FloatField(default=0)
    capacitive_power_peak_time = models.FloatField(default=0)
    capacitive_power_off_peak_time = models.FloatField(default=0)

    def save_measurements(values_list, transductor):
        """
        Method responsible to save measurements based on values
        list received.
        Args:
            values_list (list): The list with all important
            measurements values.
        Return:
            None
        """
        quartely_measurement = QuarterlyMeasurement()
        quartely_measurement.transductor = transductor

        quartely_measurement.collection_date = datetime(
            values_list[0],
            values_list[1],
            values_list[2],
            values_list[3],
            values_list[4],
            values_list[5]
        )

        quartely_measurement.generated_energy_peak_time = values_list[6]
        quartely_measurement.generated_energy_off_peak_time = values_list[7]

        quartely_measurement.consumption_peak_time = values_list[8]
        quartely_measurement.consumption_off_peak_time = values_list[9]

        quartely_measurement.inductive_power_peak_time = values_list[10]
        quartely_measurement.inductive_power_off_peak_time = values_list[11]

        quartely_measurement.capacitive_power_peak_time = values_list[12]
        quartely_measurement.capacitive_power_off_peak_time = values_list[13]

        quartely_measurement.save()


class MonthlyMeasurement(EnergyMeasurement):

    generated_energy_peak_time = models.FloatField(default=0)
    generated_energy_off_peak_time = models.FloatField(default=0)
    consumption_peak_time = models.FloatField(default=0)
    consumption_off_peak_time = models.FloatField(default=0)
    inductive_power_peak_time = models.FloatField(default=0)
    inductive_power_off_peak_time = models.FloatField(default=0)
    capacitive_power_peak_time = models.FloatField(default=0)
    capacitive_power_off_peak_time = models.FloatField(default=0)
    active_max_power_peak_time = models.FloatField(default=0)
    active_max_power_off_peak_time = models.FloatField(default=0)
    reactive_max_power_peak_time = models.FloatField(default=0)
    reactive_max_power_off_peak_time = models.FloatField(
        default=0
    )

    active_max_power_list_peak_time = ArrayField(
        HStoreField(), default=None
    )
    active_max_power_list_off_peak_time = ArrayField(
        HStoreField(), default=None
    )
    reactive_max_power_list_peak_time = ArrayField(
        HStoreField(), default=None
    )
    reactive_max_power_list_off_peak_time = ArrayField(
        HStoreField(), default=None
    )

    def save_measurements(values_list, transductor):
        """
        Method responsible to save measurements based on values
        list received.

        Args:
            values_list (list): The list with all important
            measurements values.

        Return:
            None
        """
        measurement = MonthlyMeasurement()
        measurement.transductor = transductor

        measurement.collection_date = datetime(
            values_list[0],
            values_list[1],
            values_list[2],
            values_list[3],
            values_list[4],
            values_list[5]
        )

        measurement.generated_energy_peak_time = values_list[6]
        measurement.generated_energy_off_peak_time = values_list[7]

        measurement.consumption_peak_time = values_list[8]
        measurement.consumption_off_peak_time = values_list[9]

        # FIXME - This 2 measurements comming as NaN from the transductor  
        measurement.inductive_power_peak_time = 0
        measurement.inductive_power_off_peak_time = 0

        measurement.capacitive_power_peak_time = 0
        measurement.capacitive_power_off_peak_time = 0

        measurement.active_max_power_peak_time = values_list[14]
        measurement.active_max_power_off_peak_time = values_list[15]

        measurement.reactive_max_power_peak_time = values_list[16]
        measurement.reactive_max_power_off_peak_time = values_list[17]

        # Arguments refer to initial positions of values_list information
        # Further information on transductor's Memory Map
        measurement.active_max_power_list_peak_time = \
            measurement._get_list_data(18, 34, values_list)

        measurement.active_max_power_list_off_peak_time = \
            measurement._get_list_data(22, 36, values_list)

        measurement.reactive_max_power_list_peak_time = \
            measurement._get_list_data(26, 38, values_list)

        measurement.reactive_max_power_list_off_peak_time = \
            measurement._get_list_data(30, 40, values_list)

        measurement.save()

    def _get_year(self, year, month):
        return (year - 1) if (month == 1) else year

    def _get_list_data(self, value, initial_date_position, values_list):
        max_power_list = []

        current_year = values_list[0]
        current_month = values_list[1]

        count = 0

        for i in range(0, 8, 2):

            if values_list[initial_date_position][0 + i] != 0:
                value_result = values_list[value + count]
                timestamp = \
                    datetime(
                        current_year,
                        values_list[initial_date_position][0 + i],
                        values_list[initial_date_position][1 + i],
                        values_list[initial_date_position + 1][0 + i],
                        values_list[initial_date_position + 1][1 + i]
                    )
            else:
                value_result = values_list[value + count]
                timestamp = None

            dict = {
                'value': value_result,
                'timestamp': timestamp
            }
            count += 1
            max_power_list.append(dict)
        return max_power_list
