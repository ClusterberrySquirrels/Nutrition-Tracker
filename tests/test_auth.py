from .. import create_app
from datetime import datetime

def test_login(test_client):
    response = test_client.get('/login')
    assert response.status_code == 200
    assert b"Forgot your email or password?" in response.data
    
def test_signup(test_client):
    response = test_client.get('/signup')
    assert response.status_code == 200
    assert b"You already have an account? Login here." in response.data
    
def test_signup_post(test_client):
    response = test_client.post('/signup', data=dict(
        email='fake@fakemail.com',
        name='faker',
        password='fakepass'), follow_redirects=True)
    assert b"Forgot your email or password?" in response.data
    
def test_login_post(test_client):
    response = test_client.post('/login', data=dict(
        email='fake@fakemail.com',
        password='fakepass'), follow_redirects=True)
    assert b"faker" in response.data
    
def test_profile_logged_in(test_client):
    response = test_client.get('/profile')
    assert b"faker" in response.data
    
def test_create_meal(test_client):
    response = test_client.get('/profile/meal')
    assert b"Enter a meal" in response.data
    
def test_create_meal_post(test_client):
    response = test_client.post('/profile/meal', data=dict(
    name = "TestMeal1",
        calories = 100,
        carbs = 10,
        fat = 10,
        protein = 20,
        creation_date=datetime.now()), follow_redirects=True)
    assert b"TestMeal1" in response.data
    
    
def test_logout(test_client):
    response = test_client.get('/logout', follow_redirects=True)
    assert b"Eat consciously" in response.data


    