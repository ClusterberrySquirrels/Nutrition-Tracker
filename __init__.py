# Import Python libraries
import json
import os
import sqlite3

# Import third-party libraries
from flask import (
    Flask,
    render_template,
    session,
    redirect,
    url_for,
    flash,
    request,
    Blueprint,
)
from flask_login import (
    UserMixin,
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
#from flask_wtf import FlaskForm
#from wtforms import StringField, SubmitField, BooleanField, PasswordField, validators
#from wtforms.validators import DataRequired

# define user model in the database
#class SignupForm(Form):
#    username = StringField('Username', [validators.DataRequired()])
#    name = StringField('Name', [validators.DataRequired()])
#    email = StringField('Email Address', [validators.DataRequired(),
#        validators.Email(), validators.length(min=6, max=50)])
#    password = PasswordField('New Password', [validoators.DataRequired(),
#        validators.EqualTo('confirm', message='Passwords must match') ])
#    confirm = PasswordField('Repeat Password')
#    submit = SubmitField('Submit')

# Config
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    moment = Moment(app)
    bootstrap = Bootstrap(app)
    db = SQLAlchemy(app)

    # setup Flask-Login, initialize db
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User, Meal

    #auth route blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    #non-auth route blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

