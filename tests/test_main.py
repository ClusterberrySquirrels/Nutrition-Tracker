from .. import create_app

def test_index(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Eat consciously" in response.data
    
def test_about(test_client):
    response = test_client.get('/about')
    assert response.status_code == 200
    
def test_profile_logged_out(test_client):
    response = test_client.get('/profile')
    assert response.status_code == 302
    
def test_page_not_found(test_client):
    response = test_client.get('/nonexistentpage')
    assert response.status_code == 404
    
#def test_internal_server_error(test_client):
#    response = test_client.post('/login')
#    assert response.status_code == 500