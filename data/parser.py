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


class Parser:
    def __init__(self, data):
        self.data = data

    def data_parser(self) -> List[ParseData]:
        objects = []
        for object in self.data["data"]:
            url = object["url"]
            title = object["title"]
            created_time = object["created_time"]
            city = object["location"]["city"]["name"]
            region = object["location"]["region"]["name"]
            params = object.get("params", [])

            params_values = []
            for param in params:
                param_value = param.get("value")
                if param_value is not None:
                    params_values.append(param_value)
                else:
                    params_values.append('')

            photos_url = []
            for photo in object['photos']:
                photos_url.append(photo['link'][:-19])
            if not photos_url:
                photos_url.append('')

            parsed_data = ParseData(
                    url=url,
                    title=title,
                    created_time=created_time,
                    params=params_values,
                    photos=photos_url,
                    city=city,
                    region=region,
            )
            objects.append(parsed_data)

        return objects
