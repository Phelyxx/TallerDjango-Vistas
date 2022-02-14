from datetime import datetime
from variables.logic.variables_logic import get_variable
from ..models import Measurement
import datetime
from django.utils import timezone

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    measurement.variable = get_variable(new_var["variable"])
    measurement.value = new_var["value"]
    measurement.unit = new_var["unit"]
    measurement.place = new_var["place"]
    measurement.dateTime = datetime.datetime.strptime(new_var["dateTime"], "%Y-%m-%d")
    measurement.save()
    return measurement

def create_measurement(var):
    measurement = Measurement(variable=get_variable(var["variable"]), value=var["value"],
                              unit=var["unit"], place=var["place"])
    measurement.save()
    return measurement