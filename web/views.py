from flask import Blueprint, render_template, session, request, redirect, url_for, flash
from data import fetch_data, parser
from operation import operation
from .forms import SearchByCategories, SearchApartmentForm, SearchHouseForm


views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def home_view():
    form = SearchByCategories()

    if form.validate_on_submit():
        category = form.category.data
        session["category_data"] = {
            "category": form.category.data,
            "price_min": form.price_min.data,
            "price_max": form.price_max.data,
            "region": form.region.data,
            "city": form.city.data,
        }
        if category == "1307":
            return redirect(url_for("views.search_apartment_view"))
        elif category == "1309":
            return redirect(url_for("views.search_house_view"))

    return render_template("home.html", form=form)


@views.route("/search_apartment", methods=["GET", "POST"])
def search_apartment_view():
    form = SearchApartmentForm()

    if form.validate_on_submit():
        category_data = session.get("category_data")
        if category_data:
            category = category_data["category"]
            price_min = category_data["price_min"]
            price_max = category_data["price_max"]
            region = category_data["region"]
            city = category_data["city"]

            build_type = form.build_type.data
            rooms = form.rooms.data
            furniture = form.furniture.data
            area_min = form.area_min.data
            area_max = form.area_max.data

            session.pop("category_data")

    return render_template("search_apartment.html", form=form)


@views.route("/search_house", methods=["GET", "POST"])
def search_house_view():
    form = SearchHouseForm()

    if form.validate_on_submit():
        category_data = session.get("category_data")
        if category_data:
            category = category_data["category"]
            price_min = category_data["price_min"]
            price_max = category_data["price_max"]
            region = category_data["region"]
            city = category_data["city"]

            build_type = form.build_type.data
            furniture = form.furniture.data
            area_min = form.area_min.data
            area_max = form.area_max.data
            area_plot_min = form.area_plot_min.data
            area_plot_max = form.area_plot_max.data

            session.pop("category_data")

    return render_template("search_house.html", form=form)


@views.route("/results", methods=["GET", "POST"])
def results_view():
    url = fetch_data.UrlBuilderApartment().build_url(
        limit="40",
        area_min="25",
        price_min="600",
    )
    x = parser.Parser(fetch_data.FetchData(url).fetch_data())
    d = x.data_parser()

    s = operation.return_newest_offers(d)
    z = operation.return_cheapest_offer(d)
    y = operation.return_average_price(d)
    g = operation.return_cheapest_offer_per_meter(d)
    f = operation.return_average_price_per_meter(d)
    v = operation.return_most_expensive_offer(d)
    i = operation.return_most_expensive_offer_per_meter(d)
    u = operation.return_offer_largest_area_building(d)
    l = operation.return_offer_largest_area_plot(d)

    print(url)
    return render_template(
        "results.html",
        data_list=d,
        newest_offers=s,
        cheapest_offer=z,
        average_price=y,
        cheapest_offer_per_meter=g,
        average_price_per_meter=f,
        most_expensive_offer=v,
        most_expensive_offer_per_meter=i,
        largest_area_building=u,
        largest_area_plot=l,
    )
