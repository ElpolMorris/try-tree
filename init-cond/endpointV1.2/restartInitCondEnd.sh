
#!/bin/bash

# reinicio de api de condiciones iniciales

# nos situamos en el directorio correspondiente
cd /home/epic/endpoint_initCond/endpointV1.2/

# se libera el puerto 5002
fuser -k -n tcp 5002

# se reinicia la API con la data actualizada
export FLASK_APP=initCond_endpoint1_2.py
nohup flask run --host=0.0.0.0 --port=5002 &




