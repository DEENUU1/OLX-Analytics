import fetchData
import json
from abc import abstractmethod, ABC
from dataclasses import dataclass


class Parser(ABC):
    @abstractmethod
    def data_parse(self, data):
        pass


@dataclass
class HouseData:
    url: str
    title: str
    created_time: str
    price_per_meter: str
    price: int
    building_type: str
    city: str
    region: str


class ParserHouse(Parser):
    def data_parse(self, data: dict | None):
        objects = []
        for object in data['data']:
            url = object['url']
            title = object['title']
            created_time = object['created_time']
            price_per_meter = object['params'][0]['value']['key']
            price = object['params'][2]['value']['value']
            building_type = object['params'][6]['value']['key']
            city = object['location']['city']['normalized_name']
            region = object['location']['region']['normalized_name']

            objects.append(
                HouseData(
                    url=url,
                    title=title,
                    created_time=created_time,
                    price_per_meter=price_per_meter,
                    price=price,
                    building_type=building_type,
                    city=city,
                    region=region
                ))
        return objects


url = fetchData.UrlBuilderHouse().build_url(
    limit="40",
    area_min="25",
    price_min="600",
)
x = ParserHouse()
print(x.data_parse(fetchData.FetchData(url).fetch_data()))
# print(json.dumps(fetchData.FetchData(url).fetch_data(), indent=4))
