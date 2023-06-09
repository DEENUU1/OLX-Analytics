import json
from dataclasses import dataclass

from requests import get


@dataclass
class LocalizationData:
    """
    Dataclass for storing localization data
    """

    region_id: int
    city_id: int
    city_name: str


class Localization:
    """
    Fetching licalization data from OLX API
    """

    def __init__(self, city_name: str):
        self.city_name = city_name
        self.base_url = (
            f"https://www.olx.pl/api/v1/friendly-links/query-params/{self.city_name}"
        )

    def get_localization_data(self) -> dict | None:
        response = get(self.base_url)
        if response.status_code != 200:
            return None
        return json.loads(response.content)

    def return_localization_data(self) -> LocalizationData | None:
        """
        Returning localization data
        """
        data = self.get_localization_data()
        if data:
            return LocalizationData(
                data["data"]["region_id"],
                data["data"]["city_id"],
                data["metadata"]["names"]["location"]["city"]["name"],
            )
        return None
