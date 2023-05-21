from flask_login import UserMixin

from . import db
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True)
    url = db.Column(db.String(250), unique=False)


