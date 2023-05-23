import json

import pytest
import datetime
from base.data.parser import Parser, ParseData, ParamsData
from base.operation import operation


@pytest.fixture
def apartments_test_data():
    with open("test/test_base_operation/fixtures.json") as f:
        data = json.load(f)

    parser = Parser(data)
    parsed_data = parser.data_parser()
    return parsed_data

@pytest.fixture
def houses_test_data():
    with open("test/test_base_operation/fixtures_house.json") as f:
        data = json.load(f)

    parser = Parser(data)
    parsed_data = parser.data_parser()
    return parsed_data


def test_return_newest_offers_empty_list(apartments_test_data):
    assert operation.return_newest_offers(apartments_test_data) == []

def test_return_average_price_success(apartments_test_data):
    assert operation.return_average_price(apartments_test_data) == 189375.0

def test_return_average_price_zero_division_error():
    test_data = ParseData(
        url="https://www.olx.pl/d/oferta/mieszkanie-blok-59m2-CID3-IDToKpO.html",
        title="Mieszkanie blok 59m2",
        region="Łódzkie",
        city="Bełchatów",
        params=[
            ParamsData(
                key="price_per_m",
                name="Cena za m°",
                value="4474.58 zł/m",
                value_key="4474.58"
                )
            ],
        photos=["http://randomimage.com.net"],
        created_time=datetime.date(2023, 5, 10),
        )
    assert operation.return_average_price([test_data]) == 0.0

def test_return_average_price_per_meter_success(apartments_test_data):
    assert operation.return_average_price_per_meter(apartments_test_data) == 3591.57

def test_return_offer_largest_area_plot_returns_none(apartments_test_data):
    assert operation.return_offer_largest_area_plot(apartments_test_data) == None

def test_return_offer_largest_area_plot_success(houses_test_data):
    assert (
            operation.return_offer_largest_area_plot(houses_test_data).title
            == "Sprzedam dom ul. Borowa REZERWACJA"
    )

def test_return_offer_largest_area_building(apartments_test_data):
    assert (
        operation.return_offer_largest_area_building(apartments_test_data).title
        == "sprzedam mieszkanie z garażem w Pile os. Konstancji, nowe"
    )


def test_return_most_expensive_offer_per_meter(apartments_test_data):
    assert (
        operation.return_most_expensive_offer_per_meter(apartments_test_data).title
        == "Przestronna, funkcjonalna i cicha kawalerka, 29 m2, Żoliborz"
    )


def test_return_most_expensive_offer(apartments_test_data):
    assert (
        operation.return_most_expensive_offer(apartments_test_data).title
        == "Nowoczesne mieszkanie w Centrum Warszawy"
    )
