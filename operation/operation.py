from data import parser
from typing import List
import datetime


def convert_datetime_to_date(date_time) -> datetime.date:
    date_part = date_time.split('T')[0]
    date_time = datetime.datetime.strptime(date_part, "%Y-%m-%d").date()
    return date_time


def return_newest_offers(data_list: List[parser.ParseData]) -> List[parser.ParseData]:
    current_date = datetime.date.today()
    newest_offers = []

    for data in data_list:
        if convert_datetime_to_date(data.created_time) == current_date:
            newest_offers.append(data)
    return newest_offers
