import pytest
from web import create_app, db
from datetime import datetime
from web.models import ApartmentData, HouseData, User


@pytest.fixture()
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_database.db'
    app.config["SECRET_KEY"] = "test_key"
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture
def populated_database(app):
    apartment_data_1 = ApartmentData(average_price=100000, average_price_per_sqr_m=2000, date=datetime.now())
    apartment_data_2 = ApartmentData(average_price=150000, average_price_per_sqr_m=3000, date=datetime.now())

    house_data_1 = HouseData(average_price=250000, average_price_per_sqr_m=4000, date=datetime.now())
    house_data_2 = HouseData(average_price=300000, average_price_per_sqr_m=3500, date=datetime.now())

    with app.app_context():
        db.session.add(apartment_data_1)
        db.session.add(apartment_data_2)
        db.session.add(house_data_1)
        db.session.add(house_data_2)
        db.session.commit()

        yield

        db.session.delete(apartment_data_1)
        db.session.delete(apartment_data_2)
        db.session.delete(house_data_1)
        db.session.delete(house_data_2)
        db.session.commit()
