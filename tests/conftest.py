import pytest
from werkzeug.security import generate_password_hash, check_password_hash

from .. import create_app, db
from ..models import User

@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    app.config["TESTING"] = True
    app.testing = True
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
            testUser = User(email = "tester@tester.com", password = generate_password_hash("testpass1", method='sha256'))
            db.session.add(testUser)
            db.session.commit()
            yield testing_client