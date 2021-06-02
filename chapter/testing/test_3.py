from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

        def chapter_test1(self):
            with patch('random.randrange') as r:
                r.return_value = 0
                response = self.client.get(url_for('role'))
                self.assertIn(b'Space Wolves', response.data)

class TestResponse(TestBase):

        def chapter_test2(self):
            with patch('random.randrange') as r:
                r.return_value = 1
                response = self.client.get(url_for('role'))
                self.assertIn(b'Ultramarines', response.data)

class TestResponse(TestBase):

        def chapter_test3(self):
            with patch('random.randrange') as r:
                r.return_value = 2
                response = self.client.get(url_for('role'))
                self.assertIn(b'Imperial Fists', response.data)   

class TestResponse(TestBase):

        def chapter_test4(self):
            with patch('random.randrange') as r:
                r.return_value = 3
                response = self.client.get(url_for('role'))
                self.assertIn(b'Dark Angels', response.data)