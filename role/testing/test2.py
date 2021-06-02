from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import application

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

        def test_striker_position(self):
            with patch('random.randrange') as r:
                r.return_value = 0
                response = self.client.get(url_for('role'))
                self.assertIn(b'Tactical Marine', response.data)

class TestResponse(TestBase):

        def test_striker_position(self):
            with patch('random.randrange') as r:
                r.return_value = 1
                response = self.client.get(url_for('role'))
                self.assertIn(b'Assault Marine', response.data)

class TestResponse(TestBase):

        def test_striker_position(self):
            with patch('random.randrange') as r:
                r.return_value = 2
                response = self.client.get(url_for('role'))
                self.assertIn(b'Devastator Marine', response.data)   

class TestResponse(TestBase):

        def test_striker_position(self):
            with patch('random.randrange') as r:
                r.return_value = 3
                response = self.client.get(url_for('role'))
                self.assertIn(b'Scout Marine', response.data)