from .models import User
from data import fetch_data, parser

def return_users():
    users = User.query.all()
    parse_data_list = []

    for user in users:
        user_url = user.url

        fetch_data_obj = fetch_data.FetchData(user_url)
        data = fetch_data_obj.fetch_data()

        if data is not None:
            parse_data_obj = parser.Parser(data)
            parse_data = parse_data_obj.data_parser()
            parse_data_list.extend(parse_data)

    return parse_data_list
