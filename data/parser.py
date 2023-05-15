from dataclasses import dataclass
from typing import List


@dataclass
class ParseData:
    url: str
    title: str
    created_time: str
    params: list
    photos: list
    city: str
    region: str


@dataclass
class ParamsData:
    name: str
    value: str


class Parser:
    def __init__(self, data):
        self.data = data

    def parse_params(self, params):
        parsed_params = []
        for param in params:
            name = param.get("name", "")
            value = param.get("value", {}).get("label", "")
            parsed_params.append(ParamsData(name=name, value=value))
        return parsed_params

    def data_parser(self) -> List[ParseData]:
        objects = []
        for object in self.data["data"]:
            url = object["url"]
            title = object["title"]
            created_time = object["last_refresh_time"]
            city = object["location"]["city"]["name"]
            region = object["location"]["region"]["name"]
            params = object.get("params", [])
            parsed_params = self.parse_params(params)

            photos_url = []
            for photo in object['photos']:
                photos_url.append(photo['link'][:-19])
            if not photos_url:
                photos_url.append('')

            parsed_data = ParseData(
                    url=url,
                    title=title,
                    created_time=created_time,
                    params=parsed_params,
                    photos=photos_url,
                    city=city,
                    region=region,
            )
            objects.append(parsed_data)

        return objects
