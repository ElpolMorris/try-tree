
from flask import Flask, make_response, request, jsonify
import pandas as pd
import functions as fn
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


seirhvdUSA  = pd.read_csv('seirhvdUSA.csv') # SEIRHVD
statesUSA   = pd.read_csv('statesUSA.csv') # SIR/SEIR states
countiesUSA = pd.read_csv('countiesUSA.csv') # SIR/SEIR counties

# formateando y pasando los FIPS a string
fn.fipsToStr([statesUSA, seirhvdUSA, countiesUSA])
fn.fipsFormat([statesUSA, seirhvdUSA, countiesUSA])


@app.route("/<apiRoute>", methods = ['GET','POST'])
def get_initCond(apiRoute):
    res = None
    results, new_dict = {}, {}

    if request.method == 'POST':
        form = request.get_json(force = True) 

        simulations = list(form.keys())
        for sim in simulations:
            compartments, timeInit, timeEnd, scale, spatialSelection = None, None, None, None, None
            
            compartments     = form[sim].get("compartments")
            timeInit         = form[sim].get("timeInit")
            timeEnd          = form[sim].get("timeEnd")
            scale            = form[sim].get("scale")
            spatialSelection = form[sim].get("spatialSelection")
            print("sim:", sim)
            print("Compartments:", compartments)
            print("timeInit:", timeInit)
            print("timeEnd:", timeEnd)
            print("scale:", scale)
            print("spatialSelection:", spatialSelection)


            if compartments == "SEIRHVD":
                dataset = seirhvdUSA
            else:
                if scale == "States":  # statesUSA
                    dataset = statesUSA
                elif scale == "Counties":  # countiesUSA
                    dataset = countiesUSA

            new_dict[sim] = fn.endpointResponse(apiRoute, dataset, compartments, scale, timeInit, timeEnd, spatialSelection)

    elif request.method == 'GET':
        c = 'GET'
        new_dict[c] = {'Endpoint V1.1': "WORKING..."}
    
    results = {"result": new_dict}
    res = make_response(jsonify(results))
    return res


if __name__ == '__main__':
      app.run(host = '0.0.0.0', port = 5001, debug = True)
