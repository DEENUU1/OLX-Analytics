from base.data import localization
import pytest
import json


@pytest.fixture
def localization_data():
    with open("test/test_base_data/fixtures_localization.json") as f:
        data = json.load(f)


    return data

def test_create_localization_data_object():
    localization_data = localization.LocalizationData(
        region_id=100,
        city_id=120,
        city_name="Warszawa"
    )
    assert localization_data.region_id == 100
    assert localization_data.city_id == 120
    assert localization_data.city_name == "Warszawa"

def test_localization_return_localization_data_success(localization_data):
    expected_data = localization.LocalizationData(
        region_id=localization_data["data"]["region_id"],
        city_id=localization_data["data"]["city_id"],
        city_name=localization_data["metadata"]["names"]["location"]["city"]["name"],

    )
    assert expected_data == localization.Localization('Warszawa').return_localization_data()

def test_localization_return_localization_data_fail(localization_data):
    assert localization.Localization('Warszawa123').return_localization_data() == None