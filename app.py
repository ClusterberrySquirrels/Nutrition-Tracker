from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/')
def login():
    return render_template('login.html')


def load_user(id):
    pass


@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)