from re import A
import pytest
import initCond_endpoint1_2 as app
from constants.payload_example import (
    right_payload_states,
    right_payload_counties,
    wrong_scale_states,
    wrong_scale_counties,
    wrong_init_date,
    wrong_end_date,
    wrong_compartments,
    empty_info,
    date_without_data,
)
from constants.responses import success_response, not_found_response, bad_request


@pytest.fixture()
def client():
    return app.app.test_client()


success_response = b'{"SUCCESS":"Endpoint V1.2 WORKING..."}\n'
not_found_response = b'{"error":"404 Not Found: Resource not found"}\n'


@pytest.mark.parametrize(
    "endpoint, code, message",
    [
        ("/initCond", 200, success_response),
        ("/realData", 200, success_response),
        ("/api/v0/initCond", 200, success_response),
        ("/api/v0/realData", 200, success_response),
        ("/api/v0/whatever", 404, not_found_response),
        ("/api/v0/data/info", 200, b"nothing"),
    ],
)
def test_status_code_get_calls(endpoint, code, message, client):
    get_response_endpoint = client.get(endpoint)
    assert get_response_endpoint.status_code == code
    print(get_response_endpoint.data)
    if endpoint == "/api/v0/data/info":
        pass
    else:
        assert get_response_endpoint.data == message


@pytest.mark.parametrize(
    "data, code, message",
    [
        (right_payload_states, 200, False),
        (right_payload_counties, 200, False),
        (wrong_scale_states, 400, bad_request["scale"]),
        (wrong_scale_counties, 400, bad_request["scale"]),
        (wrong_init_date, 400, bad_request["date"]),
        (wrong_end_date, 400, bad_request["date"]),
        (wrong_compartments, 400, bad_request["compartments"]),
        (wrong_compartments, 400, bad_request["compartments"]),
        (empty_info, 400, bad_request["empty"]),
        # (date_without_data, 400, bad_request["date_without_data"]),
    ],
)
def test_status_code_post_calls(data, code, message, client):
    post_response_endpoint = client.post("/api/v0/realData", json=data)
    assert post_response_endpoint.status_code == code
    if message == False:
        pass
    else:
        assert post_response_endpoint.data == message


@pytest.mark.parametrize(
    "data, code, message",
    [
        (right_payload_states, 200, False),
        (right_payload_counties, 200, False),
        (wrong_scale_states, 400, bad_request["scale"]),
        (wrong_scale_counties, 400, bad_request["scale"]),
        (wrong_init_date, 400, bad_request["date"]),
        (wrong_end_date, 400, bad_request["date"]),
        (wrong_compartments, 400, bad_request["compartments"]),
        (wrong_compartments, 400, bad_request["compartments"]),
        (empty_info, 400, bad_request["empty"]),
        (date_without_data, 400, bad_request["date_without_data"]),
    ],
)
def test_status_code_post_calls(data, code, message, client):
    post_response_endpoint = client.post("/api/v0/initCond", json=data)
    assert post_response_endpoint.status_code == code
    if message == False:
        pass
    else:
        assert post_response_endpoint.data == message
"""
    Queda pendiente: 
    - verificar respuestas de metodos http no disponibles para rutas post
"""
