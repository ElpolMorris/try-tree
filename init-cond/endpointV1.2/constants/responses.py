success_response = b'{\n  "SUCCESS": "Endpoint V1.2 WORKING..."\n}\n'
not_found_response = b'{\n  "error": "404 Not Found: Resource not found"\n}\n'
bad_request = {
    "scale": b'{\n  "error": "400 Bad Request: *ERROR. Incorrect scale"\n}\n',
    "compartments": b'{\n  "error": "400 Bad Request: *ERROR. Incorrect compartments"\n}\n',
    "date": b'{\n  "error": "400 Bad Request: *ERROR. Incorrect date format or nonexistent"\n}\n',
    "spatialSelection": b'{\n  "error": "400 Bad Request: *ERROR. Spatial selection must be an array"\n}\n',
    "limits_dates": b'{\n  "error": "400 Bad Request: *ERROR. TimeInit must be lesser than timeEnd"\n}\n',
    "date_without_data": b'{\n  "error": "400 Bad Request: *ERROR. There is not data for that date"\n}\n',
    "bad_format": b'{\n  "error": "400 Bad Request: *ERROR. Payload must be a JSON object"\n}\n',
    "empty": b'{\n  "error": "400 Bad Request: *ERROR. Payload cannot to be empty"\n}\n',
}
