from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app


class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI= "sqlite:///test.db",
            DEBUG=True,
        )
        return app

class TestResponse(TestBase):
    def test_frontend(self):
        with requests_mock.mock() as m:
            m.get("http://space-marine-chapter:5000/chapter",text="Space Wolves")
            m.get("http://space-marine-role:5000/role",text="Assault Marine")
            m.post("http://space-marine-name:5000/name",text="Ragnar Blackmane")
            response = self.client.get(url_for('index'))
            self.assertIn(b'You are Ragnar Blackmane, Assault Marine of the Emperors Space Wolves Chapter!', response.data)