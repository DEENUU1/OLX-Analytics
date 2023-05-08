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
        self.base_url = f'https://www.olx.pl/api/v1/friendly-links/query-params/{self.city_name}'

    def get_localization_data(self):
        response = get(self.base_url)
        return json.loads(response.content)

    def return_localization_data(self):
        data = self.get_localization_data()
        return LocalizationData(
            data['data']['region_id'],
            data['data']['city_id'],
            data['metadata']['names']['location']['city']['name']
        )

