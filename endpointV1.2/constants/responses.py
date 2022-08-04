success_response = b'{"SUCCESS":"Endpoint V1.2 WORKING..."}\n'
not_found_response = b'{"error":"404 Not Found: Resource not found"}\n'
bad_request = {
    "scale": b'{"error":"400 Bad Request: *ERROR. Incorrect scale"}\n',
    "compartments": b'{"error":"400 Bad Request: *ERROR. Incorrect compartments"}\n',
    "date": b'{"error":"400 Bad Request: *ERROR. Incorrect date format or nonexistent"}\n',
    "spatialSelection": b'{"error":"400 Bad Request: *ERROR. Spatial selection must be an array"}\n',
    "limits_dates": b'{"error":"400 Bad Request: *ERROR. TimeInit must be lesser than timeEnd"}\n',
    "date_without_data": b'{"error":"400 Bad Request: *ERROR. There is not data for that date"}\n',
    "bad_format": b'{"error":"400 Bad Request: *ERROR. Payload must be a JSON object"}\n',
    "empty": b'{"error":"400 Bad Request: *ERROR. Payload cannot to be empty"}\n',
}
