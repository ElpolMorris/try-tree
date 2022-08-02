from flask import abort
from datetime import datetime
import collections.abc
import numpy as np

format = '%Y-%m-%d'

def validate_datetime(dateToValidate):
    if dateToValidate is None:
        return False
    try:
        isValidated = datetime.strptime(dateToValidate,format)
        return True
    except ValueError:
        return False

def verify_request_covid_series(compartments, timeInit, timeEnd, scale, spatialSelection):
    if compartments not in ["SIR", "SEIR", "SEIRHVD"]:
        abort(400,description="*ERROR. Incorrect compartments")
    if scale not in ["States", "Counties"]:
        abort(400,description="*ERROR. Incorrect scale")
    if not validate_datetime(timeInit) or not validate_datetime(timeEnd):
         abort(400,description="*ERROR. Incorrect date format or nonexistent ")
    if not datetime.strptime(timeInit, format) or not datetime.strptime(timeInit, format):
        abort(400,description="*ERROR. Incorrect date format or nonexistent ")
    if datetime.strptime(timeInit, format) > datetime.strptime(timeEnd, format):
        abort(400, description="*ERROR. TimeInit must be lesser than timeEnd")
    if not isinstance(np.array(spatialSelection), (collections.abc.Sequence, np.ndarray)):
        abort(400, description="*ERROR. Spatial selection must be an array")