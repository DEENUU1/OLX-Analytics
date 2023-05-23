from web.models import ApartmentData, HouseData
from datetime import datetime, timedelta
from abc import ABC, abstractmethod


class Report(ABC):
    """
    Abstract class for creating weekly reports
    """

    current_date = datetime.now()
    start_date = current_date - timedelta(days=7)

    @abstractmethod
    def return_report(self):
        pass

    def return_weekly_average_price(self, data):
        """
        Counts average price for given data
        """
        sum_price = 0
        for item in data:
            sum_price += item.average_price
        return round(sum_price / len(data), 2)

    def return_weekly_average_area_price(self, data):
        """
        Counts average price for given data
        """
        sum_price = 0
        for item in data:
            sum_price += item.average_price_per_sqr_m
        return round(sum_price / len(data), 2)


class ReportApartment(Report):
    """
    Implementation of abstract class for creating weekly reports for apartments
    """

    def return_report(self):
        apartment_data = ApartmentData.query.filter(
            ApartmentData.date >= self.start_date,
            ApartmentData.date <= self.current_date,
        ).all()
        return apartment_data


class ReportHouse(Report):
    """
    Implementation of abstract class for creating weekly reports for houses
    """

    def return_report(self):
        house_data = HouseData.query.filter(
            HouseData.date >= self.start_date, HouseData.date <= self.current_date
        ).all()
        return house_data
