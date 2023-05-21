import datetime
from data.parser import convert_datetime_to_date


def test_convert_datetime_to_date():
    expected_result = datetime.date(2023, 5, 10)
    assert (
        convert_datetime_to_date("2023-05-10T15:31:26+02:00")
        == expected_result
    )