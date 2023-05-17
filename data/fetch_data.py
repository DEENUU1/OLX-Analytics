import json
from requests import get
from abc import ABC, abstractmethod


class FetchData:
    def __init__(self, url: str):
        self.url = url

    def fetch_data(self) -> dict | None:
        response = get(self.url)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None


class UrlBuilder(ABC):
    base_url = (
        "https://www.olx.pl/api/v1/offers/?offset=0&sort_by=created_at%3Adesc&limit=40"
    )

    @abstractmethod
    def build_url(self, **kwargs: str) -> str:
        pass


class UrlBuilderApartment(UrlBuilder):
    def build_url(self, **kwargs) -> str:
        parameters = {
            "category_id": "&category_id={}",
            "build_type": "&filter_enum_builttype%5B0%5D={}",
            "floor_select": "&filter_enum_floor_select%5B0%5D=floor_{}",
            "furniture": "&filter_enum_furniture%5B0%5D={}",
            "rooms": "&filter_enum_rooms%5B0%5D={}",
            "area_min": "&filter_float_m%3Afrom={}",
            "area_max": "&filter_float_m%3Ato={}",
            "price_min": "&filter_float_price%3Afrom={}",
            "price_max": "&filter_float_price%3Ato={}",
            "region_id": "&region_id={}",
            "city_id": "&city_id={}",
        }

        for key, value in parameters.items():
            argument = kwargs.get(key)
            if argument:
                if key == "floor_select":
                    self.base_url += value.format(argument)
                else:
                    self.base_url += value.format(argument)

        return self.base_url


class UrlBuilderHouse(UrlBuilder):
    def build_url(self, **kwargs) -> str:
        parameters = {
            "build_type": "&filter_enum_builttype%5B0%5D={}",
            "market_type": "&filter_enum_market[0]=primary={}",
            "furniture": "&filter_enum_furniture%5B0%5D={}",
            "floor_count": "&filter_enum_floor%5B0%5D={}",
            "area_min": "&filter_float_area%3Afrom={}",
            "area_max": "&filter_float_area%3Ato={}",
            "plot_area_min": "&filter_float_m%3Ato={}",
            "plot_area_max": "&filter_float_price%3Afrom={}",
            "price_per_m_min": "&filter_float_price_per_m%3Afrom={}",
            "price_per_m_max": "&filter_float_price_per_m%3Ato={}",
            "price_min": "&filter_float_price%3Afrom={}",
            "price_max": "&filter_float_price%3Ato={}",
            "region_id": "&region_id={}",
            "city_id": "&city_id={}",
        }

        for key, value in parameters.items():
            argument = kwargs.get(key)
            if argument:
                self.base_url += value.format(argument)

        self.base_url += f"&category_id=3"

        return self.base_url
