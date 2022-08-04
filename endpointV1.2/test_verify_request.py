from utils.verify_request_covid_series import validate_datetime

def test_validate_datetime_function_sucess():
    isTrue = validate_datetime("2021-05-29")
    wrong_format_date = validate_datetime("2021-05-32")
    empty_date = validate_datetime()
    assert isTrue == True
    assert wrong_format_date == False
    assert empty_date == False
