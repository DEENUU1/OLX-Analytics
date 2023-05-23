import datetime
from base.data.parser import convert_datetime_to_date, ParamsData, ParseData, Parser
import json
import pytest

@pytest.fixture
def data_to_parse():
    with open("base/operation/test/fixtures.json") as f:
        data = json.load(f)


    return data

def test_convert_datetime_to_date() -> None:
    expected_result = datetime.date(2023, 5, 10)
    assert convert_datetime_to_date("2023-05-10T15:31:26+02:00") == expected_result

def test_parser_data_parser_return_params_data_objects(data_to_parse):
    parser = Parser(data_to_parse)
    params_data_1 = ParamsData(
        key="price_per_m",
        name="Cena za m²",
        value="4474.58 zł/m²",
        value_key="4474.58"
    )
    assert parser.data_parser()[0].params[0] == params_data_1
    assert parser.data_parser()[0].url == "https://www.olx.pl/d/oferta/mieszkanie-blok-59m2-CID3-IDToKpO.html"
    assert parser.data_parser()[0].title == "Mieszkanie blok 59m2"
    assert parser.data_parser()[0].region == "Łódzkie"
    assert parser.data_parser()[0].city == "Bełchatów"

def test_create_params_data_object() -> None:
    params_data = ParamsData(
        key="price_per_m",
        name="Cena za m°",
        value="4474.58 zł/m",
        value_key="4474.58"
    )
    assert params_data.key == "price_per_m"
    assert params_data.name == "Cena za m°"
    assert params_data.value == "4474.58 zł/m"
    assert params_data.value_key == "4474.58"


def test_create_parse_data_object() -> None:
    parse_data = ParseData(
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
    assert parse_data.url == "https://www.olx.pl/d/oferta/mieszkanie-blok-59m2-CID3-IDToKpO.html"
    assert parse_data.title == "Mieszkanie blok 59m2"
    assert parse_data.region == "Łódzkie"
    assert parse_data.city == "Bełchatów"
    assert parse_data.params[0].key == "price_per_m"

