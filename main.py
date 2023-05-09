from data import fetchData
from data import localization


def main():
    url = fetchData.UrlBuilderHouse().build_url(
        limit="40",
        area_min="25",
        price_min="600",
    )

    print(fetchData.UrlBuilderHouse().fetch_data(url))


if __name__ == "__main__":
    print(main())