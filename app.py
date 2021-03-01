import os
from flask import Flask, render_template, session, redirect, url_for, flash  # pip install flask
from flask_bootstrap import Bootstrap  # pip install flask-bootstrap
from flask_moment import Moment  # pip install flask-moment
from flask_wtf import FlaskForm  # pip install flask-wtf
from wtforms import StringField, SubmitField  # pip install flask-wtf
from wtforms.validators import DataRequired  # pip install flask-wtf
from flask_sqlalchemy import SQLAlchemy  # pip install flask-sqlalchemy

""" 
To install Flask in the virtual environment, make sure the venv virtual environment
is activated and then install flask using the pip command.

When you want to start using the virtual environment, you have to activate it.  
    Linux: source venv/bin/activate
    Windows: venv \ Scripts \ activate   <--- Space intentional in this example 
                                              for formatting reasons. Don't leave
                                              the space in when you go to execute.
                                              
When you are done working with the virtual environment, type "deactivate" at the 
command prompt to restore the PATH environment variable for your terminal session
and the command prompt to their original states.               

To start the app.py application, make sure the virtual environment is activated.

    Linux: $ export FLASK_APP=app.py  <--- To run in debug mode include:  
           $ flask run                     $ export FLASK_DEBUG=1  
    Windows: $ set FLASK_APP=app.py        for the next command. 
             $ flask run
             
Once the server starts up, it goes into a loop that accepts requests and services them.
Press Ctrl+C to quit.

When the server is running, open your web browser and type http://localhost:5000/       

"""
basedir = os.path.abspath(os.path.dirname(__file__))

################# Initialize and configure a SQLite database###################
# The URL of the app database must be configures as the key SQLALCHEMY_DATABASE_URI
# in the Flask config object.  The Flask-SQLAlchemy documentation also suggests
# setting key SQLALCHEMY_TRACK_MODIFICATIONS to False to use less memory unless
# signals for object changes are needed.  Consult the Flask SQLAlchemy docs for
# info on other config options.
# The db object instantiated from the class SQLAlchemy represents the database
# and provides access to all the functionality of Flask-SQLAlchemy.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)  # Bootstrap initialization
moment = Moment(app)  # Moment initialization
db = SQLAlchemy(app)  # SQLAlchemy init


# Handles application URL functions.
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False))


# Error handler returns a numeric status code that corresponds to the error.
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def login():
    return render_template('login.html')


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Error handler returns a numeric status code that corresponds to the error.
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


########################## Role and User definitions ##########################
# The term models used when referring to the persistent entities used by the
# application. In the context of an object relational map, a model is a Python
# class with attributes that match the columns of a corresponding database table.
# The db instance from Flask-SQLAlchemy provides a base class for models as well
# as a set of helper classes and functions that are used to define their structure.
# __tablename__ class defines the name of the table in the db.
#
# Flask-SQLAlchemy assigns a default table name if __tablename__ is omitted, but
# those default names do not follow the popular convention of using plurals for
# table names, so it is best to name tables explicitly.  The remaining class
# variables are the attributes of the model, defined as instances of the db.Column
# class.

# The first argument given to the db.Column constructor is the type of the db
# column and model attribute.  Check out the SQLAlchemy docs for other column
# types that can be used.
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


# role_id to db.ForeignKey() specifies that the col should be interpreted as
# having id values from rows in the roles table.

# The backref argument to db.relationship() defines the reverse direction of the
# relationship, by addin ga role attribute to the User model.  This attribute
# can be used on any instance of User insted of the role_id foreign key to
# access the Role model as an object.
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username
