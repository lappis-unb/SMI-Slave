from django.db import models
from datetime import datetime
from transductor.models import EnergyTransductor
from boogie.rest import rest_api

class MinutelyMeasurement(models.Model):

    frequency_a = models.FloatField(default=None)
    voltage_a  = models.FloatField(default=None)
    voltage_b = models.FloatField(default=None)
    voltage_c = models.FloatField(default=None)
    current_a = models.FloatField(default=None)
    current_b = models.FloatField(default=None)
    current_c = models.FloatField(default=None)
    active_power_a = models.FloatField(default=None)
    active_power_b = models.FloatField(default=None)
    active_power_c = models.FloatField(default=None)
    total_active_power = models.FloatField(default=None)
    reactive_power_a = models.FloatField(default=None)
    reactive_power_b = models.FloatField(default=None)
    reactive_power_c = models.FloatField(default=None)
    total_reactive_power_a = models.FloatField(default=None)
    apparent_power_a = models.FloatField(default=None)
    apparent_power_b = models.FloatField(default=None)
    apparent_power_c = models.FloatField(default=None)
    total_apparent_power = models.FloatField(default=None)
    power_factor_a = models.FloatField(default=None)
    power_factor_b = models.FloatField(default=None)
    power_factor_c = models.FloatField(default=None)
    total_power_factor = models.FloatField(default=None)
    dht_voltage_a = models.FloatField(default=None)
    dht_voltage_b = models.FloatField(default=None)
    dht_voltage_c = models.FloatField(default=None)
    dht_current_a = models.FloatField(default=None)
    dht_current_b = models.FloatField(default=None)
    dht_current_c = models.FloatField(default=None)

    def get_measure():
        pass

    # def save_measurements(values_list, transductor):
    # """
    # Method responsible to save measurements based on values
    # list received.
    # Args:
    #     values_list (list): The list with all important
    #     measurements values.
    # Return:
    #     None
    # """
    # measurement = MinutelyMeasurement()
    # measurement.transductor = transductor
    
    # frequency_a = values_list[]
    # voltage_a  = values_list[]
    # voltage_b = values_list[]
    # voltage_c = values_list[]
    # current_a = values_list[]
    # current_b = values_list[]
    # current_c = values_list[]
    # active_power_a = values_list[]
    # active_power_b = values_list[]
    # active_power_c = values_list[]
    # total_active_power = values_list[]
    # reactive_power_a = values_list[]
    # reactive_power_b = values_list[]
    # reactive_power_c = values_list[]
    # total_reactive_power_a = values_list[]
    # apparent_power_a = values_list[]
    # apparent_power_b = values_list[]
    # apparent_power_c = values_list[]
    # total_apparent_power = values_list[]
    # power_factor_a = values_list[]
    # power_factor_b = values_list[]
    # power_factor_c = values_list[]
    # total_power_factor = values_list[]
    # dht_voltage_a = values_list[]
    # dht_voltage_b = values_list[]
    # dht_voltage_c = values_list[]
    # dht_current_a = values_list[]
    # dht_current_b = values_list[]
    # dht_current_c = values_list[]

    # measurement.save()

class QuarterlyMeasurement(models.Model):
    
    generated_energy_peak_time = models.FloatField(default=None)
    generated_energy_off_peak_time = models.FloatField(default=None)
    consumption_peak_time = models.FloatField(default=None)
    consumption_off_peak_time = models.FloatField(default=None)
    inductive_power_peak_time = models.FloatField(default=None)
    inductive_power_off_peak_time = models.FloatField(default=None)
    capacitive_power_peak_time = models.FloatField(default=None)
    capacitive_power_off_peak_time = models.FloatField(default=None)

    def get_measure():
        pass
    
    # def save_measurements(values_list, transductor):
    # """
    # Method responsible to save measurements based on values
    # list received.
    # Args:
    #     values_list (list): The list with all important
    #     measurements values.
    # Return:
    #     None
    # """
    # measurement = QuarterlyMeasurement()
    # measurement.transductor = transductor
    
    # generated_energy_peak_time = values_list[]
    # generated_energy_off_peak_time = values_list[]
    # consumption_peak_time = values_list[]
    # consumption_off_peak_time = values_list[]
    # inductive_power_peak_time = values_list[]
    # inductive_power_off_peak_time = values_list[]
    # capacitive_power_peak_time = values_list[]
    # capacitive_power_off_peak_time = values_list[]

    # measurement.save()

class MonthlyMeasurement(models.Model):

    generated_energy_peak_time = models.FloatField(default=None)
    generated_energy_off_peak_time = models.FloatField(default=None)
    consumption_peak_time = models.FloatField(default=None)
    consumption_off_peak_time = models.FloatField(default=None)
    inductive_power_peak_time = models.FloatField(default=None)
    inductive_power_off_peak_time = models.FloatField(default=None)
    capacitive_power_peak_time = models.FloatField(default=None)
    capacitive_power_off_peak_time = models.FloatField(default=None)
    active_max_power_peak_time = models.FloatField(default=None)
    active_max_power_off_peak_time = models.FloatField(default=None)
    reactive_max_power_peak_time = models.FloatField(default=None)
    reactive_max_power_off_peak_time = models.FloatField(default=None)

    def get_measure():
        pass

    # def save_measurements(values_list, transductor):
    #     """
    #     Method responsible to save measurements based on values
    #     list received.

    #     Args:
    #         values_list (list): The list with all important
    #         measurements values.

    #     Return:
    #         None
    #     """
    #     measurement = MonthlyMeasurement()
    #     measurement.transductor = transductor

    #     generated_energy_peak_time = values_list[]
    #     generated_energy_off_peak_time = values_list[]
    #     consumption_peak_time = values_list[]
    #     consumption_off_peak_time = values_list[]
    #     inductive_power_peak_time = values_list[]
    #     inductive_power_off_peak_time = values_list[]
    #     capacitive_power_peak_time = values_list[]
    #     capacitive_power_off_peak_time = values_list[]
    #     active_max_power_peak_time = values_list[]
    #     active_max_power_off_peak_time = values_list[]
    #     reactive_max_power_peak_time = values_list[]
    #     reactive_max_power_off_peak_time = values_list[]

    #     measurement.save()

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

        consumption_a (float): The total consumption on phase A. (since last reset)
        consumption_b (float): The total consumption on phase B. (since last reset)
        consumption_c (float): The total consumption on phase C. (since last reset)
        total_consumption (float): The total consumption of transductor. (since last reset)

    """
    transductor = models.ForeignKey(
        EnergyTransductor,related_name="measurements", on_delete=models.CASCADE
    )

    def __str__(self):
        return '%s' % self.collection_date

    def get_time_measurements():
        measures = [
            MinuteMeasurement.objects.all(),
            HourMeasurement.objects.all(),
            QuarterMeasurement.objects.all()
        ]
        return measures
