import json

import pytest

from base.data.parser import Parser
from base.operation import operation


@pytest.fixture
def offers_test_data():
    with open("test/test_base_operation/fixtures.json") as f:
        data = json.load(f)

    parser = Parser(data)
    parsed_data = parser.data_parser()
    return parsed_data


def test_return_average_price(offers_test_data):
    assert operation.return_average_price(offers_test_data) == 189375.0


def test_return_average_price_per_meter(offers_test_data):
    assert operation.return_average_price_per_meter(offers_test_data) == 3591.57


def test_return_offer_largest_area_plot(offers_test_data):
    assert operation.return_offer_largest_area_plot(offers_test_data) == None


def test_return_offer_largest_area_building(offers_test_data):
    assert (
        operation.return_offer_largest_area_building(offers_test_data).title
        == "sprzedam mieszkanie z garażem w Pile os. Konstancji, nowe"
    )


def test_return_most_expensive_offer_per_meter(offers_test_data):
    assert (
        operation.return_most_expensive_offer_per_meter(offers_test_data).title
        == "Przestronna, funkcjonalna i cicha kawalerka, 29 m2, Żoliborz"
    )


def test_return_most_expensive_offer(offers_test_data):
    assert (
        operation.return_most_expensive_offer(offers_test_data).title
        == "Nowoczesne mieszkanie w Centrum Warszawy"
    )
