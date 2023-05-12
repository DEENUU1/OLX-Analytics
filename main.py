from data import fetch_data
from data import parser
from operation import save_data


def main():
    url = fetch_data.UrlBuilderHouse().build_url(
        limit="40",
        area_min="25",
        price_min="600",
    )
    x = parser.Parser(fetch_data.FetchData(url).fetch_data())
    d = x.data_parser()
    for y in d:
        print(y.url)
        print(y.title)
    save_data.save_to_excel(d, 'dane.xlsx')


if __name__ == "__main__":
    print(main())
