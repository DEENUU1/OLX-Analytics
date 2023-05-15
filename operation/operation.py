from data import parser
from typing import List
import datetime


def convert_datetime_to_date(date_time) -> datetime.date:
    date_part = date_time.split("T")[0]
    date_time = datetime.datetime.strptime(date_part, "%Y-%m-%d").date()
    return date_time


def return_newest_offers(data_list: List[parser.ParseData]) -> List[parser.ParseData]:
    current_date = datetime.date.today()
    newest_offers = []

    for data in data_list:
        if convert_datetime_to_date(data.created_time) == current_date:
            newest_offers.append(data)
    return newest_offers


def return_cheapest_offer(data_list: List[parser.ParseData]) -> parser.ParseData:
    lowest_price_object = None
    lowest_price = float("inf")

    for data in data_list:
        for param in data.params:
            if param.name == "Cena":
                price_str = param.value.replace(" ", "")
                try:
                    price = float(price_str[:-2])
                    if price < lowest_price:
                        lowest_price = price
                        lowest_price_object = data
                except ValueError:
                    pass
    return lowest_price_object


def return_average_price(data_list: List[parser.ParseData]) -> float:
    total_price = 0
    for data in data_list:
        for param in data.params:
            if param.name == "Cena":
                price_str = param.value.replace(" ", "")
                try:
                    price = float(price_str[:-2])
                    total_price += price
                except ValueError:
                    pass
    return round(total_price / len(data_list), 2)
