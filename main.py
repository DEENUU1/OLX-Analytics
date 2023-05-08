from data import fetchData
from data import localization


def main():
    url = fetchData.UrlBuilderHouse().build_url(
        limit="40",
        floor_select="1",
        furniture="yes",
        rooms="two",
        area_min="25",
        price_min="600",
        price_max="1500"
    )

    print(fetchData.UrlBuilderHouse().fetch_data(url))


if __name__ == "__main__":
    print(main())