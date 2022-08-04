from tkinter import N, W
from flask import abort
from datetime import datetime
import collections.abc
import numpy as np

format = "%Y-%m-%d"


def validate_datetime(dateToValidate=None):
    if dateToValidate is None:
        return False
    try:
        isValidated = datetime.strptime(dateToValidate, format)
        return True
    except ValueError:
        return False


def verify_request_covid_series(
    compartments, timeInit, timeEnd, scale, spatialSelection
):
    if not compartments or not timeInit or not scale or not spatialSelection:
        abort(400, description="*ERROR. payload properites cannot be empty")
    if compartments not in ["SIR", "SEIR", "SEIRHVD"]:
        abort(400, description="*ERROR. Incorrect compartments")
    if scale not in ["States", "Counties"]:
        abort(400, description="*ERROR. Incorrect scale")
    if not validate_datetime(timeInit) or not validate_datetime(timeEnd):
        abort(400, description="*ERROR. Incorrect date format or nonexistent")
    if not datetime.strptime(timeInit, format) or not datetime.strptime(
        timeInit, format
    ):
        abort(400, description="*ERROR. Incorrect date format or nonexistent")
    if datetime.strptime(timeInit, format) > datetime.strptime(timeEnd, format):
        abort(400, description="*ERROR. TimeInit must be lesser than timeEnd")
    if not isinstance(
        np.array(spatialSelection), (collections.abc.Sequence, np.ndarray)
    ):
        abort(400, description="*ERROR. Spatial selection must be an array")


def verify_right_properties_in_payload(whitelist: list, data: dict):
    if not data:
        abort(400, description="*ERROR. Payload cannot to be empty")
    if type(data) is not dict:
        abort(400, description="*ERROR. Payload must be a JSON object")
    if type(whitelist) is not list:
        abort(500, description="*ERROR. Internal error, please try again later")
