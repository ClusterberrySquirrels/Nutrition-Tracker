from flask import Flask
import app
from flask_testing import TestCase
import unittest


class BaseTestCase(TestCase):
    """A base test case"""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

# your test cases

class FlaskTestCase(unittest.TestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        # tester = main.test_client(self)
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
