from dataclasses import dataclass
from typing import List
import datetime


@dataclass
class ParamsData:
    """
    Dataclass for params
    """

    key: str
    name: str
    value: str
    value_key: str


@dataclass
class ParseData:
    """
    Dataclass for parsed data
    """

    url: str
    title: str
    created_time: datetime.date
    params: List[ParamsData]
    photos: List[str]
    city: str
    region: str


def convert_datetime_to_date(date_time) -> datetime.date:
    date_part = date_time.split("T")[0]
    date_time = datetime.datetime.strptime(date_part, "%Y-%m-%d").date()
    return date_time


class Parser:
    def __init__(self, data):
        self.data = data

    def parse_params(self, params):
        parsed_params = []
        for param in params:
            name = param.get("name", "")
            key = param.get("key", "")
            value = param.get("value", {}).get("label", "")
            value_key = param.get("value", {}).get("key", "")
            parsed_params.append(
                ParamsData(name=name, value=value, key=key, value_key=value_key)
            )
        return parsed_params

    def data_parser(self) -> List[ParseData]:
        objects = []
        for object in self.data["data"]:
            url = object["url"]
            title = object["title"]
            created_time = convert_datetime_to_date(object["last_refresh_time"])
            city = object["location"]["city"]["name"]
            region = object["location"]["region"]["name"]
            params = object.get("params", [])
            parsed_params = self.parse_params(params)

            photos_url = []
            for photo in object["photos"]:
                photos_url.append(photo["link"][:-19])
            if not photos_url:
                photos_url.append("")

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
