import datetime
from typing import List

from base.data import parser


def return_newest_offers(data_list: List[parser.ParseData]) -> List[parser.ParseData]:
    current_date = datetime.date.today()
    newest_offers = []

    for data in data_list:
        if data.created_time == current_date:
            newest_offers.append(data)
    return newest_offers


def get_price_value(data) -> float | None:
    for param in data.params:
        if param.key == "price":
            price_str = param.value.replace(" ", "")
            try:
                return float(price_str[:-2])
            except ValueError:
                pass
    return None


def get_param_value(data, key):
    value = 0
    for param in data.params:
        if param.key == key:
            value_str = param.value_key.replace(" ", "")
            try:
                value = float(value_str)
            except ValueError:
                pass
    return value


def return_most_expensive_offer(
    data_list: List[parser.ParseData],
) -> parser.ParseData | None:
    max_price_object = None
    max_price = 0

    for obj in data_list:
        for param in obj.params:
            if param.key == "price":
                price = param.value.replace(" zł", "").replace(" ", "")
                if price.isdigit() and int(price) > max_price:
                    max_price = int(price)
                    max_price_object = obj

    return max_price_object


def return_most_expensive_offer_per_meter(
    data_list: List[parser.ParseData],
) -> parser.ParseData | None:
    max_price_per_meter = 0
    max_price_per_meter_obj = None

    for data in data_list:
        for param in data.params:
            if param.key == "price_per_m":
                price_per_meter = float(param.value_key)
                if price_per_meter > max_price_per_meter:
                    max_price_per_meter = price_per_meter
                    max_price_per_meter_obj = data

    return max_price_per_meter_obj


def return_offer_largest_area_building(
    data_list: List[parser.ParseData],
) -> parser.ParseData | None:
    max_area = 0
    max_area_object = None

    for data in data_list:
        for param in data.params:
            if param.key == "m":
                area_str = param.value.split(" ")[0]
                area = int(area_str.replace(",", ""))
                if area > max_area:
                    max_area = area
                    max_area_object = data
                break

    return max_area_object


def return_offer_largest_area_plot(
    data_list: List[parser.ParseData],
) -> parser.ParseData | None:
    max_area = 0
    max_area_object = None

    for data in data_list:
        for param in data.params:
            if param.key == "area":
                area_str = param.value.split(" ")[0]
                area = int(area_str.replace(",", ""))
                if area > max_area:
                    max_area = area
                    max_area_object = data
                break

    return max_area_object


def return_average_price(data_list: List[parser.ParseData]) -> float:
    total_price = 0
    count = 0

    for data in data_list:
        price = get_price_value(data)
        if price is not None:
            total_price += price
            count += 1
    try:
        calculate_avg_price = round(total_price / count, 2)
    except ZeroDivisionError:
        calculate_avg_price = 0.0
    return calculate_avg_price


def return_average_price_per_meter(data_list: List[parser.ParseData]) -> float:
    total_price = 0
    count = 0

    for data in data_list:
        price = get_param_value(data, "price_per_m")
        total_price += price
        count += 1
    try:
        calculate_avg_price = round(total_price / count, 2)
    except ZeroDivisionError:
        calculate_avg_price = 0.0
    return calculate_avg_price
