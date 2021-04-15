from datetime import datetime
from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from .models import Meal
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
    meals = current_user.show_meals().all()
    return render_template('profile.html', name=current_user.name, meals=meals)

@main.route('/profile/meal')
@login_required
def create_meal():
    return render_template('meal.html')

@main.route('/profile/meal', methods=['POST'])
@login_required
def create_meal_post():
    meal = Meal(
        name = request.form.get('name'),
        calories = request.form.get('calories'),
        carbs = request.form.get('carbs'),
        fat = request.form.get('fat'),
        protein = request.form.get('protein'),
        user_id=current_user.id,
        creation_date=datetime.now(),
    )
    db.session.add(meal)
    db.session.commit()
    return redirect(url_for('main.profile'))

@main.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
