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


def get_price_value(data):
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
                value = float(value_str[:-2])
            except ValueError:
                pass
    return value


def find_extreme_offer(data_list, key, compare_func):
    extreme_offer = None
    extreme_value = compare_func(0, float("inf"))

    for data in data_list:
        value = get_param_value(data, key)
        if compare_func(value, extreme_value):
            extreme_value = value
            extreme_offer = data

    return extreme_offer


def return_average_price(data_list):
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


def return_average_price_per_meter(data_list):
    total_price = 0
    count = 0

    for data in data_list:
        price = get_param_value(data, "price_per_m")
        total_price += price
        count += 1
    try:
        calculate_avg_price = round(total_price / count, 2)
    except:
        calculate_avg_price = 0.0
    return calculate_avg_price


def return_most_expensive_offer(data_list):
    return find_extreme_offer(data_list, "price", max)


def return_most_expensive_offer_per_meter(data_list):
    return find_extreme_offer(data_list, "price_per_m", max)


def return_offer_largest_area_building(data_list):
    return find_extreme_offer(data_list, "m", max)


def return_offer_largest_area_plot(data_list):
    return find_extreme_offer(data_list, "area", max)
