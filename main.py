import json
import requests
import urllib
import ast
from urllib.parse import unquote
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
    if request.form.get("foodsearch"):
        food = request.form.get('food')
        amount = request.form.get('amount')
        query = urllib.parse.quote(food)
        response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key=y2hXFh3cw60yrPltEjUklm0fo9zHOkNb2NEE9Fzw&query=' + query + '&pageSize=8')
        foodData = json.loads(response.text)
        results = []
        for foods in foodData['foods']:
            try:
                results.append({"name": foods['description'], "brand": foods['brandOwner'], "id": foods['fdcId']})
            except KeyError:
                results.append({"name": foods['description'], "brand": "", "id": foods['fdcId']})
        return redirect(url_for('main.search_foods', foods=results, amount=amount))
        
@main.route('/profile/meal/foods/<foods>/<amount>')
@login_required
def search_foods(foods, amount):
    result = ast.literal_eval(foods)
    return render_template('foods.html', foods=result, amount=amount)

@main.route('/profile/meal/foods/<foods>/<amount>', methods=['POST'])
@login_required
def search_foods_post(foods, amount):
    response = request.form['submitFood']
    foodResponse = requests.get('https://api.nal.usda.gov/fdc/v1/food/' + response + '?api_key=y2hXFh3cw60yrPltEjUklm0fo9zHOkNb2NEE9Fzw')
    foodData = json.loads(foodResponse.text)
    amount = float(amount)
    for nutrients in foodData['foodNutrients']:
        if "Energy" in nutrients['nutrient']['name']:
            try:
                calories = (float(nutrients['amount']) / 100) * amount
            except KeyError:
                calories = 0
        if "fat" in nutrients['nutrient']['name']:
            try:
                fat = (float(nutrients['amount']) / 100) * amount
            except KeyError:
                fat = 0
        if "Carb" in nutrients['nutrient']['name']:
            try:
                carbs = (float(nutrients['amount']) / 100) * amount
            except KeyError:
                carbs = 0
        if "Protein" in nutrients['nutrient']['name']:
            try:
                protein = (float(nutrients['amount']) / 100) * amount
            except KeyError:
                protein = 0
    try:
        brand = foodData['brandOwner']
    except KeyError:
        brand = ""
    food = Meal(
        name = foodData['description'],
        brand = brand,
        calories = round(calories, 2),
        fat = round(fat, 2),
        carbs = round(carbs, 2),
        protein = round(protein, 2),
        creation_date = datetime.now(),
        user_id = current_user.id,
        )
    db.session.add(food)
    db.session.commit()
    return redirect(url_for('main.profile'))

@main.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
