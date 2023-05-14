from flask import Blueprint, render_template, request, redirect, url_for, flash


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')