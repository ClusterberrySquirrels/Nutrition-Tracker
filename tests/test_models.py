from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash

def test_new_user():
    user = User(email='noahlaratta@gmail.com', name='Noah Laratta', password=generate_password_hash('TestPass1', method='sha256'))
    assert user.email == 'noahlaratta@gmail.com'
    assert user.name=='Noah Laratta'
    assert user.password != 'TestPass1'