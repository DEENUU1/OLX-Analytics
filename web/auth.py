from flask import Blueprint, render_template, redirect, url_for, request, flash

from web import db
from .models import User
from .forms import RegisterForm
from data import fetch_data
from data import localization

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    localization_data = localization.Localization(form.city.data)
    if form.validate_on_submit():
        if form.category.data == "1307":
            url_builder = fetch_data.UrlBuilderApartment()
            url = url_builder.build_url(
                city_id=localization_data.return_localization_data().city_id,
                region_id=localization_data.return_localization_data().region_id,
            )
            new_user = User(email=form.email.data, url=url)
            db.session.add(new_user)
            db.session.commit()
            flash("Welcome on the website", category="success")
            return redirect(url_for("views.home_view"))

        elif form.category.data == "1309":
            url_builder = fetch_data.UrlBuilderHouse()
            url = url_builder.build_url(
                city_id=localization_data.return_localization_data().city_id,
                region_id=localization_data.return_localization_data().region_id,
            )
            new_user = User(email=form.email.data, url=url)
            db.session.add(new_user)
            db.session.commit()
            flash("Welcome on the website", category="success")
            return redirect(url_for("views.home_view"))

    return render_template("auth/register.html", form=form)
