import pytest

from base.data import fetch_data


def test_apartment_build_url_success() -> None:
    url = fetch_data.UrlBuilderApartment().build_url(city_id="1")
    assert (
        url
        == "https://www.olx.pl/api/v1/offers/?offset=0&sort_by=created_at%3Adesc&limit=40&city_id=1&category_id=1307"
    )


def test_house_build_url_success() -> None:
    url = fetch_data.UrlBuilderHouse().build_url(city_id="1")
    assert (
        url
        == "https://www.olx.pl/api/v1/offers/?offset=0&sort_by=created_at%3Adesc&limit=40&city_id=1&category_id=1309"
    )


@pytest.mark.parametrize(
    "url",
    [
        "https://www.olx.pl/api/v1/offers/?offset=0&sort_by=created_at%3Adesc&limit=40&city_id=1&category_id=1309",
    ],
)
def test_fetch_data_success(url) -> None:
    fetcher = fetch_data.FetchData(url)
    data = fetcher.fetch_data()
    assert data is not None
