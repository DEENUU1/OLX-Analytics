import json
from requests import get
from dataclasses import dataclass


@dataclass
class LocalizationData:
    region_id: int
    city_id: int
    city_name: str


class Localization:
    def __init__(self, city_name: str):
        self.city_name = city_name
        self.base_url = (
            f"https://www.olx.pl/api/v1/friendly-links/query-params/{self.city_name}"
        )

    def get_localization_data(self):
        try:
            response = get(self.base_url)
            response.raise_for_status()
            return json.loads(response.content)
        except Exception as e:
            print(e)
            return None

    def return_localization_data(self):
        data = self.get_localization_data()
        if data:
            try:
                return LocalizationData(
                    data["data"]["region_id"],
                    data["data"]["city_id"],
                    data["metadata"]["names"]["location"]["city"]["name"],
                )
            except Exception as e:
                print(e)
                return None
        else:
            return None
