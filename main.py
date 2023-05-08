from data import fetchData
from data import localization


def main():
    url = fetchData.UrlBuilderApartment().build_url(
        limit="40",
        category_id="15",
        build_type="blok",
        floor_select="1",
        furniture="yes",
        rooms="one",
        area_min="25",
        area_max="50",
        price_min="600",
        price_max="3000"
    )

    print(fetchData.UrlBuilderApartment().get_data(url))


if __name__ == "__main__":
    print(main())