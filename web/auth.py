from flask import Blueprint, render_template, redirect, url_for, flash

from web import db
from .models import User
from .forms import RegisterForm, DeleteAccountForm, validate_city_name
from base.data import fetch_data, localization
from base.email import send_email
from datetime import datetime

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        localization_data = localization.Localization(validate_city_name(form.city.data)).return_localization_data()
        if localization_data is None:
            flash("City not found", category="error")
            return redirect(url_for("auth.register"))

        if form.category.data == "1307":
            url_builder = fetch_data.UrlBuilderApartment()
        else:
            url_builder = fetch_data.UrlBuilderHouse()

        url = url_builder.build_url(
            city_id=localization_data.city_id,
            region_id=localization_data.region_id,
        )

        new_user = User(
            email=form.email.data,
            url=url,
            weekly_report=form.weekly_report.data,
            date=datetime.utcnow(),
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Your account has been created", category="success")

        send_email(
            "Thank you for registering on our website",
            "Visit my GitHub: https://github.com/DEENUU1",
            form.email.data,
        )

        return redirect(url_for("views.home_view"))

    return render_template("auth/register.html", form=form, email_error=form.errors.get("email"))


@auth.route("/delete", methods=["POST", "GET"])
def delete_account():
    form = DeleteAccountForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        send_email(
            "Your account has been deleted",
            "Visit my GitHub: https://github.com/DEENUU1",
            form.email.data,
        )

        db.session.delete(user)
        db.session.commit()

        flash("Your account has been deleted", category="success")

        return redirect(url_for("views.home_view"))

    return render_template("auth/delete_account.html", form=form, email_error=form.errors.get("email"))
