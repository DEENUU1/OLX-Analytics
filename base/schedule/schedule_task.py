from web.models import User, ApartmentData, HouseData
from base.data import parser
from base.data import fetch_data
from web.email import send_email
from web import create_app
from base.operation import operation
from web import db

def send_newest_offers():
    with create_app().app_context():
        users = User.query.all()
        send_email_objs = []

        for user in users:
            user_url = user.url

            fetch_data_obj = fetch_data.FetchData(user_url)
            data = fetch_data_obj.fetch_data()

            if data is not None:
                parse_data_obj = parser.Parser(data)
                parse_data = parse_data_obj.data_parser()
                send_email_obj = send_email("Dane", parse_data, user.email)
                send_email_objs.append(send_email_obj)

        return send_email_objs


def schedule_report():
    with create_app().app_context():

        apartments_url = fetch_data.UrlBuilderApartment().build_url()
        houses_url = fetch_data.UrlBuilderHouse().build_url()

        parse_apartments = parser.Parser(fetch_data.FetchData(apartments_url).fetch_data()).data_parser()
        parse_houses = parser.Parser(fetch_data.FetchData(houses_url).fetch_data()).data_parser()

        apartments_average_price = operation.return_average_price(parse_apartments)
        apartments_average_price_per_sqr_m = operation.return_average_price_per_meter(parse_apartments)

        houses_average_price = operation.return_average_price(parse_houses)
        houses_average_price_per_sqr_m = operation.return_average_price_per_meter(parse_houses)


        apartments_data = ApartmentData(
            average_price=apartments_average_price,
            average_price_per_sqr_m=apartments_average_price_per_sqr_m,
        )

        db.session.add(apartments_data)
        db.session.commit()

        houses_data = HouseData(
            average_price=houses_average_price,
            average_price_per_sqr_m=houses_average_price_per_sqr_m,
        )

        db.session.add(houses_data)
        db.session.commit()

    return apartments_data, houses_data

