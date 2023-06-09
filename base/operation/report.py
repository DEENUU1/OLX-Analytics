from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import Any

from web.models import ApartmentData, HouseData


class Report(ABC):
    """
    Abstract class for creating weekly reports
    """

    @abstractmethod
    def return_report(self):
        pass

    @staticmethod
    def return_weekly_average_price(data) -> float:
        """
        Counts average price for given data
        """
        sum_price = sum(item.average_price for item in data)
        try:
            return round(sum_price / len(data), 2)
        except ZeroDivisionError:
            return 0.0

    @staticmethod
    def return_weekly_average_area_price(data) -> float:
        """
        Counts average price for given data
        """
        sum_price = sum(item.average_price_per_sqr_m for item in data)
        try:
            return round(sum_price / len(data), 2)
        except ZeroDivisionError:
            return 0.0


class ReportApartment(Report):
    """
    Implementation of abstract class for creating weekly reports for apartments
    """

    def return_report(self) -> Any:
        current_date = datetime.now()
        start_date = current_date - timedelta(days=7)
        apartment_data = ApartmentData.query.filter(
            ApartmentData.date >= start_date,
            ApartmentData.date <= current_date,
        ).all()
        return apartment_data


class ReportHouse(Report):
    """
    Implementation of abstract class for creating weekly reports for houses
    """

    def return_report(self) -> Any:
        current_date = datetime.now()
        start_date = current_date - timedelta(days=7)
        house_data = HouseData.query.filter(
            HouseData.date >= start_date, HouseData.date <= current_date
        ).all()
        return house_data
