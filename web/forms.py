from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


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

    category = SelectField("Category", choices=CATEGORIES, default="")
    price_min = SelectField("Price min", choices=PRICE_VALUES, default="")
    price_max = SelectField("Price max", choices=PRICE_VALUES, default="")
    city = StringField("City", default="")


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

    build_type = SelectField("Build type", choices=BUILD_TYPE, default="")
    furniture = SelectField("Furniture", choices=FURNITURE, default="")
    rooms = SelectField("Rooms", choices=ROOMS, default="")
    area_min = SelectField("Area min", choices=AREA_VALUES, default="")
    area_max = SelectField("Area max", choices=AREA_VALUES, default="")


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
        ("35", "35"),
        ("60", "60"),
        ("80", "80"),
        ("100", "100"),
        ("125", "125"),
        ("150", "150"),
        ("175", "175"),
        ("225", "225"),
        ("350", "350"),
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
