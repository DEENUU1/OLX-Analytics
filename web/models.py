from flask_login import UserMixin

from . import db
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True)
    url = db.Column(db.String(250), unique=False)
    weekly_report = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime, default=datetime.now())


class ApartmentData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    average_price = db.Column(db.Float, unique=False)
    average_price_per_sqr_m = db.Column(db.Float, unique=False)
    date = db.Column(db.DateTime, default=datetime.now())


class HouseData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    average_price = db.Column(db.Float, unique=False)
    average_price_per_sqr_m = db.Column(db.Float, unique=False)
    date = db.Column(db.DateTime, default=datetime.now())
