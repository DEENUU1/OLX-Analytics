from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, EmailField, TextAreaField
from wtforms.validators import InputRequired, Length, ValidationError
from .models import User
from unidecode import unidecode


def validate_city_name(city):
    city_clear_polish_char = unidecode(str(city))
    city_count_words = city_clear_polish_char.split()

    if len(city_count_words) == 1:
        return city_clear_polish_char
    return "-".join(city_count_words)

class SearchByCategories(FlaskForm):
    CATEGORIES = [("1307", "Apartments"), ("1309", "Houses")]
    PRICE_VALUES = [
        ("1000", "1000"),
        ("2000", "2000"),
        ("3000", "3000"),
        ("100000", "100000"),
        ("150000", "150000"),
        ("200000", "200000"),
        ("300000", "300000"),
    ]

    category = SelectField("Category", choices=CATEGORIES)
    price_min = SelectField("Price min", choices=PRICE_VALUES)
    price_max = SelectField("Price max", choices=PRICE_VALUES)
    city = StringField("City", validators=[InputRequired()], default=None, render_kw={"placeholder": "City name"})


class SearchApartmentForm(FlaskForm):
    BUILD_TYPE = [
        ("blok", "Blok"),
        ("kamienica", "Kamienica"),
        ("szeregowiec", "Szeregowiec"),
        ("loft", "Loft"),
        ("pozostałe", "Pozostałe"),
    ]
    FURNITURE = [("wszystkie", "Wszystkie"), ("tak", "Tak"), ("nie", "Nie")]
    ROOMS = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4+"),
    ]
    AREA_VALUES = [
        ("25", "25"),
        ("40", "40"),
        ("50", "50"),
        ("60", "60"),
        ("70", "70"),
        ("80", "80"),
        ("100", "100"),
        ("120", "120"),
        ("150", "150"),
    ]

    build_type = SelectField("Build type", choices=BUILD_TYPE)
    furniture = SelectField("Furniture", choices=FURNITURE)
    rooms = SelectField("Rooms", choices=ROOMS)
    area_min = SelectField("Area min", choices=AREA_VALUES)
    area_max = SelectField("Area max", choices=AREA_VALUES)


class SearchHouseForm(FlaskForm):
    BUILD_TYPE = [
        ("wolnostojacy", "Wolnostojący"),
        ("blizniak", "Bliźniak"),
        ("szeregowiec", "Szeregowiec"),
        ("gospodarstwo", "Gospodarstwo"),
        ("letniskowy", "Letniskowy"),
        ("pozostałe", "Pozostałe"),
    ]
    AREA_VALUES = [
        ("30", "30"),
        ("60", "60"),
        ("90", "90"),
        ("125", "125"),
        ("150", "150"),
        ("175", "175"),
        ("225", "225"),
        ("250", "250"),
        ("500", "500"),
    ]
    AREA_PLOT_VALUES = [
        ("500", "500"),
        ("1000", "1000"),
        ("1500", "1500"),
        ("2000", "2000"),
        ("2500", "2500"),
        ("3000", "3000"),
    ]
    build_type = SelectField("Category", choices=BUILD_TYPE)
    area_min = SelectField("Area min", choices=AREA_VALUES)
    area_max = SelectField("Area max", choices=AREA_VALUES)
    area_plot_min = SelectField("Area plo mint", choices=AREA_PLOT_VALUES)
    area_plot_max = SelectField("Area plot max", choices=AREA_PLOT_VALUES)


class RegisterForm(FlaskForm):
    CATEGORIES = [("1307", "Apartments"), ("1309", "Houses")]

    email = EmailField(validators=[InputRequired()], render_kw={"placeholder": "Email"})
    category = SelectField(validators=[InputRequired()], choices=CATEGORIES)
    city = StringField(
        validators=[InputRequired()], render_kw={"placeholder": "City name"}
    )

    def validate_email(self, email):
        """This method is checking if email already exist in database"""
        existing_user_email = User.query.filter_by(email=email.data).first()
        if existing_user_email:
            raise ValidationError(
                "That email already exists. Please choose a different one."
            )


class DeleteAccountForm(FlaskForm):
    email = EmailField(validators=[InputRequired()], render_kw={"placeholder": "Email"})

    def validate_email(self, email):
        """This method is checking if email already exist in database"""
        existing_user_email = User.query.filter_by(email=email.data).first()
        if not existing_user_email:
            raise ValidationError(
                "That email does not exist. Please choose a different one."
            )
