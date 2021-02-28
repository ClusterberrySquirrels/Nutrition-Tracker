from flask import Flask, render_template, abort
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


# @app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1>Hello, {}</h1>'.format(user.name) # TODO: define name reference


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def login():
    return render_template('login.html')


def load_user(id): # TODO: define id
    pass


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Keyword user/name represents the argument name used int he placeholder written in the template
# <name> is a variable in the current scope that provides the value for the argument of the same name.
# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name=name)
