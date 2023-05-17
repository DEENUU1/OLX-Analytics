import os

from dotenv import load_dotenv
from flask import Flask
from flask_wtf.csrf import CSRFProtect

load_dotenv()


def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect()
    csrf.init_app(app)
    app.secret_key = "develop"

    from .views import views

    app.register_blueprint(views)

    return app
