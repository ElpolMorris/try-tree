import requests

dictToSend = {"sim1": {
                "compartments": "SIR",
                "timeInit": "2021-01-31",
                # "timeEnd": "2020-06-26",
                "scale": "States", 
                "spatialSelection": ["13", "15"]
              }#,
              # "sim2": {
              #   "compartments": "SEIR",
              #   "timeInit": "2021-08-25",
              #   "timeEnd": "2021-09-27",
              #   "scale": "Counties", 
              #   "spatialSelection": ["36001", "36003"]
              # },
              # "sim3": {
              #   "compartments": "SEIRHVD",
              #   "timeInit": "2021-07-10",
              #   "timeEnd": "2021-07-11",
              #   "scale": "States", 
              #   "spatialSelection": ["13", "15", "17"]
              # },
              # "sim4": {
              #   "compartments": "SEIRHVD",
              #   "timeInit": "2021-09-15",
              #   "timeEnd": "2021-09-16",
              #   "scale": "Counties", 
              #   "spatialSelection": ["36001", "36003"]
              # }
              }
              
# # route = "realData"
# for k in list(dictToSend.keys()):
#   try:
#     t_final = dictToSend[k]['timeEnd']
#   except:
#     t_final = dictToSend[k]['timeInit']

#   if t_final == dictToSend[k]['timeInit']:
#     route = 'initCond'
#   elif t_final == dictToSend[k]['timeEnd']:
#     route = 'realData'

# res = requests.post(url, json = dictToSend)
res = requests.post('http://127.0.0.1:5002/initCond', json = dictToSend)
# res = requests.post('http://192.168.2.131:2/' + route, json = dictToSend)
print(res.content)
print("status_code", res.status_code)
