import datetime
import json

import pytest

from data.parser import Parser
from operation import operation


def test_convert_datetime_to_date():
    expected_result = datetime.date(2023, 5, 10)
    assert (
        operation.convert_datetime_to_date("2023-05-10T15:31:26+02:00")
        == expected_result
    )


@pytest.fixture
def offers_test_data():
    with open("operation/test/fixtures.json") as f:
        data = json.load(f)

    parser = Parser(data)
    parsed_data = parser.data_parser()
    return parsed_data


def test_return_average_price(offers_test_data):
    assert operation.return_average_price(offers_test_data) == 189375.0


def test_return_average_price_per_meter(offers_test_data):
    assert operation.return_average_price_per_meter(offers_test_data) == 2627.17


def test_return_offer_largest_area_plot(offers_test_data):
    assert (
        operation.return_offer_largest_area_plot(offers_test_data).title
        == "Mieszkanie blok 59m2"
    )


def test_return_offer_largest_area_building(offers_test_data):
    assert (
        operation.return_offer_largest_area_building(offers_test_data).title
        == "Duże Mieszkanie 63 M2 W Szczecinie Na Osiedlu Zawa"
    )


def test_return_most_expensive_offer_per_meter(offers_test_data):
    assert (
        operation.return_most_expensive_offer_per_meter(offers_test_data).title
        == "Bezpośrednio od właściciela  - blisko POLITECHNIKI"
    )


def test_return_most_expensive_offer(offers_test_data):
    assert (
        operation.return_most_expensive_offer(offers_test_data).title
        == "Mieszkanie blok 59m2"
    )
