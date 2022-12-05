import requests

dictToSend = {"compartments":"SEIR","timeInit":"2020-06-25", "scale":"Counties", "spatialSelection":["36001", "36003"]}
res = requests.post('http://192.168.2.131:5000/initCond', json = dictToSend)
print(res.content)