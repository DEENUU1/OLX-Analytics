from web.models import User, ApartmentData, HouseData
from datetime import datetime

def test_create_user_object():
    user = User(
        email="test@example.com",
        url="https://www.example.com",
        weekly_report=0,
        date=datetime.utcnow(),
    )
    assert user.email == "test@example.com"
    assert user.url == "https://www.example.com"
    assert isinstance(user.weekly_report, int)

def test_create_apartment_data_object():
    apartment_data = ApartmentData(
        average_price=9321.32,
        average_price_per_sqr_m=3123.3,
        date=datetime.utcnow(),
    )
    assert apartment_data.average_price == 9321.32
    assert apartment_data.average_price_per_sqr_m == 3123.3
    assert isinstance(apartment_data.date, datetime)


def test_create_house_data_object():
    house_data = HouseData(
        average_price=9321.32,
        average_price_per_sqr_m=3123.3,
        date=datetime.utcnow(),
    )
    assert house_data.average_price == 9321.32
    assert house_data.average_price_per_sqr_m == 3123.3
    assert isinstance(house_data.date, datetime)

