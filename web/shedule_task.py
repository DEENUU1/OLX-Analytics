from .models import User
from data import fetch_data, parser
from .email import send_email

def return_users():
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


