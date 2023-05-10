from data import fetchData
from data import parser


def main():
    url = fetchData.UrlBuilderHouse().build_url(
        limit="40",
        area_min="25",
        price_min="600",
    )
    x = parser.ParserHouse()
    print(url)
    print(x.data_parse(fetchData.FetchData(url).fetch_data())[1])


if __name__ == "__main__":
    print(main())