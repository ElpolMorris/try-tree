from operator import itemgetter
from flask import Flask, abort, make_response, request, jsonify
from datetime import datetime
import pandas as pd
import utils.functions1_2 as fn
from utils.verify_request_covid_series import (
    verify_request_covid_series,
    verify_right_properties_in_payload,
)
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# df_info = pd.read_csv('Codes_USA', dtype={'FIPS_state': str,'FIPS_county': str})

seirhvdUSA = pd.read_csv(
    "../endpoint_docs/seirhvd_initCond_by_state.csv", dtype={"FIPS_state": str}
)  # SEIRHVD
statesUSA = pd.read_csv(
    "../endpoint_docs/seir_initCond_by_states.csv", dtype={"FIPS_state": str}
)  # SIR/SEIR states
countiesUSA = pd.read_csv(
    "../endpoint_docs/seir_initCond_by_county.csv", dtype={"FIPS_county": str}
)  # SIR/SEIR counties


@app.route("/<apiRoute>", methods=["GET", "POST"])
def get_initCond(apiRoute):

    res, new_dict, status_code = None, {}, 0
    flagTimeInit, flagTimeEnd = False, False

    if request.method == "POST":

        form = request.get_json(force=True)
        simulations = list(form.keys())
        for sim in simulations:

            compartments = form[sim].get("compartments")
            timeInit = form[sim].get("timeInit")
            timeEnd = form[sim].get("timeEnd")
            scale = form[sim].get("scale")
            spatialSelection = form[sim].get("spatialSelection")
            print("sim:", sim)
            print("Compartment:", compartments)
            print("timeInit:", timeInit)
            print("timeEnd:", timeEnd)
            print("scale:", scale)
            print("spatialSelection:", spatialSelection)

            # RESTRICCIONES Y ERRORES
            if apiRoute not in ["initCond", "realData"]:
                new_dict[apiRoute] = "ERROR. Incorrect route"
                abort(404, description="Resource not found")

            # compartment validation
            if compartments not in ["SIR", "SEIR", "SEIRHVD"]:
                new_dict[compartments] = "ERROR. Incorrect compartments"

            # scale validation
            if scale not in ["States", "Counties"]:
                new_dict[scale] = "ERROR. Incorrect scale"

            # timeInit validation
            try:
                datetime.strptime(timeInit, "%Y-%m-%d")
                flagTimeInit = True
                if datetime.strptime(timeInit, "%Y-%m-%d") > datetime.strptime(
                    timeEnd, "%Y-%m-%d"
                ):
                    abort(400, description="timeInit must be lesser than timeEnd")
            except ValueError:
                abort(
                    400,
                    description="ERROR. Incorrect format or nonexistent timeInit or timeEnd",
                )
                # new_dict[timeInit] = "ERROR. Incorrect format or nonexistent timeInit"

            # timeEnd validation
            if timeEnd is None:
                timeEnd = timeInit
                flagTimeEnd = True
            else:
                try:
                    datetime.strptime(timeEnd, "%Y-%m-%d")
                    flagTimeEnd = True
                except ValueError:
                    abort(
                        400,
                        description="ERROR. Incorrect format or nonexistent timeInit or timeEnd",
                    )

            status_code = 404

            # valid condition
            if (
                (apiRoute in ["initCond", "realData"])
                and (compartments in ["SIR", "SEIR", "SEIRHVD"])
                and (scale in ["States", "Counties"])
                and flagTimeInit
                and flagTimeEnd
            ):
                if compartments == "SEIRHVD":
                    dataset = seirhvdUSA
                else:
                    if scale == "States":  # statesUSA
                        dataset = statesUSA
                    elif scale == "Counties":  # countiesUSA
                        dataset = countiesUSA

                new_dict[sim] = fn.endpointResponse(
                    apiRoute,
                    dataset,
                    compartments,
                    scale,
                    timeInit,
                    timeEnd if apiRoute == "realDate" else timeInit,
                    spatialSelection,
                )
                status_code = 200

    elif request.method == "GET":
        if apiRoute not in ["initCond", "realData"]:
            abort(404, description="Resource not found")
        new_dict["SUCCESS"] = "Endpoint V1.2 WORKING..."
        status_code = 200

    res = (
        jsonify(
            new_dict,
        ),
        status_code,
    )
    return make_response(res)


@app.route("/api/v0/data/info", methods=["GET"])
def get_data_info():
    min_max_dates_by_us_dataframe = {
        "seirhvdUSA": {
            "min": sorted(seirhvdUSA.DateTime.to_list())[0],
            "max": sorted(seirhvdUSA.DateTime.to_list())[-1],
        },
        "statesUSA": {
            "min": sorted(statesUSA.DateTime.to_list())[0],
            "max": sorted(statesUSA.DateTime.to_list())[-1],
        },
        "countiesUSA": {
            "min": sorted(countiesUSA.DateTime.to_list())[0],
            "max": sorted(countiesUSA.DateTime.to_list())[-1],
        },
    }
    return make_response(jsonify(min_max_dates_by_us_dataframe), 200)


@app.route("/api/v0/<apiRoute>", methods=["GET", "POST"])
def get_initCond2(apiRoute):
    res, got_covid_series = None, {}
    if apiRoute not in ["initCond", "realData"]:
        abort(404, description="Resource not found")
    if request.method == "POST":
        requested_covid_series = request.get_json(force=True)
        verify_right_properties_in_payload(
            ["scale", "compartments", "timeInit", "spatialSelection"],
            requested_covid_series,
        )
        series_names = list(requested_covid_series.keys())

        # Processing each requested_covid_series
        for index, requested_serie in enumerate(requested_covid_series.values()):
            compartments, timeInit, timeEnd, scale, spatialSelection = itemgetter(
                "compartments", "timeInit", "timeEnd", "scale", "spatialSelection"
            )(requested_serie)
            # validating series attributes
            verify_request_covid_series(
                compartments, timeInit, timeEnd, scale, spatialSelection
            )

            if compartments == "SEIRHVD":
                dataset = seirhvdUSA
            else:
                if scale == "States":  # statesUSA
                    dataset = statesUSA
                elif scale == "Counties":  # countiesUSA
                    dataset = countiesUSA
            got_covid_series[series_names[index]] = fn.endpointResponse(
                apiRoute,
                dataset,
                compartments,
                scale,
                timeInit,
                timeEnd if apiRoute == "realData" else timeInit,
                spatialSelection,
            )
            

    elif request.method == "GET":
        if apiRoute not in ["initCond", "realData"]:
            abort(404, description="Resource not found")
        got_covid_series["SUCCESS"] = "Endpoint V1.2 WORKING..."

    res = (
        jsonify(
            got_covid_series,
        ),
        200,
    )
    return make_response(res)


@app.errorhandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(405)
def not_found(e):
    return jsonify(error=str(e)), 405


@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error=str(e)), 500
