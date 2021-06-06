from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

        def test_role1(self):
            for _ in range(10):
                response = self.client.get(url_for('chapter'))
                self.assertIn(response.data.decode(),["Space Wolves", "Ultramarines", "Imperial Fists", "Dark Angels", "Salamanders", "Blood Angels"])

