from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
