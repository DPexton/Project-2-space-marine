from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def frontend_test(self):
        with patch('requests.get') as a:
            with patch('requests.post') as b:
                a.return_value.text = "Space Wolves"
                b.return_value.text = "Ragnar Blackmane"
                response = self.client.get(url_for('index'))
                self assertIn(b'Ragnar Blackmane, the Assault Marine of the Emperors Space Wolves Chapter!')
