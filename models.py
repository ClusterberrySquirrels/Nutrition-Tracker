from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    # Foreign key relationship to meals
    meals = db.relationship('Meal', backref='user', lazy='dynamic')
    
    def show_meals(self):
        return Meal.query.filter_by(user_id=self.id)
    
class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String(1000), nullable=False)
    brand = db.Column(db.String(1000))
    amount = db.Column(db.Float)
    calories = db.Column(db.Float)
    carbs = db.Column(db.Float)
    fat = db.Column(db.Float)
    protein = db.Column(db.Float)
    # Foreign key relationship to users
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)