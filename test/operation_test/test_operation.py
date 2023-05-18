import datetime

import pytest

import json

from operation import operation


@pytest.fixture
def offers_fixtures():
    with open("fixtures.json") as f:
        return json.load(f)


def test_convert_datetime_to_date():
    expected_result = datetime.date(2023, 5, 10)
    assert (
        operation.convert_datetime_to_date("2023-05-10T15:31:26+02:00")
        == expected_result
    )
