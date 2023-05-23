from web.models import User, ApartmentData, HouseData
from base.data import parser
from base.data import fetch_data
from base.email import send_email
from web import create_app
from base.operation import operation
from web import db
from datetime import datetime
from base.operation import report


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

        apartments_data = process_data(apartments_url, parse_apartments=True)
        houses_data = process_data(houses_url, parse_apartments=False)

        db.session.add(apartments_data)
        db.session.add(houses_data)
        db.session.commit()

    return apartments_data, houses_data


def process_data(url, parse_apartments):
    data = parser.Parser(fetch_data.FetchData(url).fetch_data()).data_parser()
    average_price = operation.return_average_price(data)
    average_price_per_sqr_m = operation.return_average_price_per_meter(data)
    datetime_now = datetime.utcnow()

    if parse_apartments:
        return ApartmentData(
            average_price=average_price,
            average_price_per_sqr_m=average_price_per_sqr_m,
            date=datetime_now,
        )
    else:
        return HouseData(
            average_price=average_price,
            average_price_per_sqr_m=average_price_per_sqr_m,
            date=datetime_now,
        )


def send_weekly_reports_to_users():
    with create_app().app_context():
        users = User.query.filter(User.weekly_report == 1).all()
        send_email_objs = []

        for user in users:
            report_apartment = report.ReportApartment().return_report()
            report_house = report.ReportHouse().return_report()

            report_apartment_str = stringify_report(report_apartment)
            report_house_str = stringify_report(report_house)

            email_content = f"Raport dla apartamentów:\n{report_apartment_str}\n\nRaport dla domów:\n{report_house_str}"

            send_email_obj = send_email(
                "Tygodniowe podsumowanie", email_content, user.email
            )
            send_email_objs.append(send_email_obj)

        return send_email_objs


def stringify_report(report):
    report_str = ""
    for data in report:
        report_str += f"Średnia cena: {data.average_price}\n"
        report_str += (
            f"Średnia cena za metr kwadratowy: {data.average_price_per_sqr_m}\n"
        )
        report_str += f"Data: {data.date}\n\n"

    return report_str
