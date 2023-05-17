from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


class SearchByCategories(FlaskForm):
    CATEGORIES = [("1307", "Apartments"), ("1309", "Houses")]
    category = SelectField("Category", choices=CATEGORIES)
    price_min = StringField("Price min")
    price_max = StringField("Price max")
    region = StringField("Region")
    city = StringField("City")


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
