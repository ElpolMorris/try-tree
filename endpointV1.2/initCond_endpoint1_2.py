
from flask import Flask, make_response, request, jsonify
from datetime import datetime
import pandas as pd
import functions1_2 as fn
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


seirhvdUSA  = pd.read_csv('../endpoint_docs/seirhvdUSA.csv') # SEIRHVD
statesUSA   = pd.read_csv('../endpoint_docs/statesUSA.csv') # SIR/SEIR states
countiesUSA = pd.read_csv('../endpoint_docs/countiesUSA.csv') # SIR/SEIR counties

# formateando y pasando los FIPS a string
fn.fipsToStr([statesUSA, seirhvdUSA, countiesUSA])
fn.fipsFormat([statesUSA, seirhvdUSA, countiesUSA])


@app.route("/<apiRoute>", methods = ['GET','POST'])
def get_initCond(apiRoute):

    res, new_dict, status_code = None, {}, 0
    flagTimeInit, flagTimeEnd = False, False

    if request.method == 'POST':

        form = request.get_json(force = True) 
        sim = list(form.keys())[0]
            
        compartments     = form[sim].get("compartments")
        timeInit         = form[sim].get("timeInit")
        timeEnd          = form[sim].get("timeEnd")
        scale            = form[sim].get("scale")
        spatialSelection = form[sim].get("spatialSelection")
        print("sim:", sim)
        print("Compartment:", compartments)
        print("timeInit:", timeInit)
        print("timeEnd:", timeEnd)
        print("scale:", scale)
        print("spatialSelection:", spatialSelection)

        #restrictions
        if apiRoute not in ["initCond", "realData"]:
            new_dict[apiRoute] = "ERROR. Incorrect route"

        # compartment validation
        if compartments not in ["SIR", "SEIR", "SEIRHVD"]:
            new_dict[compartments] = "ERROR. Incorrect compartments"

        # scale validation
        if scale not in ["States", "Counties"]:
            new_dict[scale] = "ERROR. Incorrect scale"

        # timeInit validation
        try:
            datetime.strptime(timeInit, '%Y-%m-%d')
            flagTimeInit = True
        except ValueError:
            new_dict[timeInit] = "ERROR. Incorrect format or nonexistent timeInit"

        # timeEnd validation
        if timeEnd is None:
            timeEnd = timeInit
            flagTimeEnd = True
        else:
            try:
                datetime.strptime(timeEnd, '%Y-%m-%d')
                flagTimeEnd = True
            except ValueError:
                new_dict[timeEnd] = "ERROR. Incorrect format or nonexistent timeEnd"

        # if scale == "States":
        #     for fips in spatialSelection:
        #         print(fips, len(fips))
        #         if len(fips) != 2:
        #             new_dict[spatialSelection] = "ERROR. One or more FIPS have incorrect format"
        #             break
        # elif scale == "Counties":
        #     for fips in spatialSelection:
        #         print(fips, len(fips))
        #         if len(fips) != 5:
        #             new_dict[spatialSelection] = "ERROR. One or more FIPS have incorrect format"
        #             break

        status_code = 404

        # valid condition
        if ((apiRoute in ["initCond", "realData"]) and 
        (compartments in ["SIR", "SEIR", "SEIRHVD"]) and 
        (scale in ["States", "Counties"])
         and flagTimeInit and flagTimeEnd):
            if compartments == "SEIRHVD":
                dataset = seirhvdUSA
            else:
                if scale == "States":  # statesUSA
                    dataset = statesUSA
                elif scale == "Counties":  # countiesUSA
                    dataset = countiesUSA

            new_dict[sim] = fn.endpointResponse(apiRoute, dataset, compartments, scale, timeInit, timeEnd, spatialSelection)
            status_code = 200

    elif request.method == 'GET':
        new_dict["SUCCESS"] = "Endpoint V1.2 WORKING..."
        status_code = 200

    res = jsonify(new_dict,), status_code
    return make_response(res)


if __name__ == '__main__':
      app.run(host = '0.0.0.0', port = 5002, debug = True)
