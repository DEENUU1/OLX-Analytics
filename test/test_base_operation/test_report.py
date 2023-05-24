from web.models import ApartmentData
from base.operation.report import Report, ReportApartment, ReportHouse
from test.test_app_config import populated_database, app, client


def test_return_weekly_average_price_apartment_data():
    data = [
        ApartmentData(average_price=100),
        ApartmentData(average_price=150),
        ApartmentData(average_price=200)
    ]
    expected_average_price = 150.0

    assert Report.return_weekly_average_price(data) == expected_average_price


def test_return_weekly_average_area_price_apartment_data():
    data = [
        ApartmentData(average_price_per_sqr_m=50),
        ApartmentData(average_price_per_sqr_m=75),
        ApartmentData(average_price_per_sqr_m=100)
    ]
    expected_average_area_price = 75.0

    assert Report.return_weekly_average_area_price(data) == expected_average_area_price


def test_return_report_apartment_data(populated_database):
    assert len(ReportApartment().return_report()) == 2
    assert ReportApartment().return_report()[0].average_price == 100000.0
    assert ReportApartment().return_report()[0].average_price_per_sqr_m == 2000.0


def test_return_house_apartment_data(populated_database):
    assert len(ReportHouse().return_report()) == 2
    assert ReportHouse().return_report()[0].average_price == 250000.0
    assert ReportHouse().return_report()[0].average_price_per_sqr_m == 4000.0
