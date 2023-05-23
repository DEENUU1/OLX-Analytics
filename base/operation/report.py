from web.models import ApartmentData, HouseData
from datetime import datetime, timedelta
from abc import ABC, abstractmethod


class Report(ABC):
    """
    Abstract class for creating weekly reports
    """

    @abstractmethod
    def return_report(self):
        pass

    @staticmethod
    def return_weekly_average_price(self, data):
        """
        Counts average price for given data
        """
        sum_price = sum(item.average_price for item in data)
        return round(sum_price / len(data), 2)

    @staticmethod
    def return_weekly_average_area_price(self, data):
        """
        Counts average price for given data
        """
        sum_price = sum(item.average_price_per_sqr_m for item in data)
        return round(sum_price / len(data), 2)

class ReportApartment(Report):
    """
    Implementation of abstract class for creating weekly reports for apartments
    """

    def return_report(self):
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

    def return_report(self):
        current_date = datetime.now()
        start_date = current_date - timedelta(days=7)
        house_data = HouseData.query.filter(
            HouseData.date >= start_date, HouseData.date <= current_date
        ).all()
        return house_data