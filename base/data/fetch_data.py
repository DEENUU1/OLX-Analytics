import json
from abc import ABC, abstractmethod

from requests import get


class FetchData:
    """
    Fetches data from the given URL.
    """

    def __init__(self, url: str):
        self.url = url

    def fetch_data(self) -> dict | None:
        """
        Fetches data from the given URL.

        Returns:
            dict: JSON data.
        """
        response = get(self.url)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None


class UrlBuilder(ABC):
    """
    Abstract class for building URL.
    """

    BASE_URL = (
        "https://www.olx.pl/api/v1/offers/?offset=0&sort_by=created_at%3Adesc&limit=40"
    )

    @abstractmethod
    def build_url(self, **kwargs: str) -> str:
        """
        Abstract method for building URL.

        Returns:
            str: URL.
        """
        pass


class UrlBuilderApartment(UrlBuilder):
    """
    Class for building URL for apartments.
    """

    def build_url(self, **kwargs) -> str:
        parameters = {
            "build_type": "&filter_enum_builttype%5B0%5D={}",
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
                self.BASE_URL += value.format(argument)

        self.BASE_URL += f"&category_id=1307"

        return self.BASE_URL


class UrlBuilderHouse(UrlBuilder):
    """
    Class for building URL for houses.
    """

    def build_url(self, **kwargs) -> str:
        parameters = {
            "build_type": "&filter_enum_builttype%5B0%5D={}",
            "area_min": "&filter_float_m%3Afrom={}",
            "area_max": "&filter_float_m%3Ato={}",
            "plot_area_min": "&filter_float_m%3Ato={}",
            "plot_area_max": "&filter_float_price%3Afrom={}",
            "price_min": "&filter_float_price%3Afrom={}",
            "price_max": "&filter_float_price%3Ato={}",
            "region_id": "&region_id={}",
            "city_id": "&city_id={}",
        }

        for key, value in parameters.items():
            argument = kwargs.get(key)
            if argument:
                self.BASE_URL += value.format(argument)

        self.BASE_URL += f"&category_id=1309"

        return self.BASE_URL
