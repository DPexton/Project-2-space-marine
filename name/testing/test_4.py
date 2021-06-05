from flask import url_for
from flask_testing import TestCase
import requests_mock
from unittest.mock import patch
from app import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):
    test_cases={
       'Space Wolves,Tactical Marine': b"Grimolf Ulfsson",
       'Space Wolves,Assault Marine': b"Ragnar Blackmane",
       'Space Wolves,Devastator Marine': b"Gunbjorn Ironmaw",
       'Space Wolves,Scout Marine': b"One-Eye Frodi",
       'Ultramarines,Tactical Marine': b"Titus Grimaldus",
       'Ultramarines,Assault Marine': b"Maximus Tarimus",
       'Ultramarines,Devastator Marine': b"Jonah Sidonis",
       'Ultramarines,Scout Marine': b"Barachiel Sadros",
       'Imperial Fists,Tactical Marine': b"Shal Cestros",
       'Imperial Fists,Assault Marine': b"Uziel Aryabhon",
       'Imperial Fists,Devastator Marine': b"Klordath Aglibesco",
       'Imperial Fists,Scout Marine': b"Kazryn Batariar",
       'Dark Angels,Tactical Marine': b"Baelar Sadross",
       'Dark Angels,Assault Marine': b"Gabriel Manuzanus",
       'Dark Angels,Devastator Marine': b"Lutheon Alcane",
       'Dark Angels,Scout Marine': b"Cassias Gabrun"
    }
    def test_spacewolves1(self):
        for data,result in self.test_cases.items():
            response = self.client.post(
                url_for('name'),
                data = data
                )
            self.assertIn(result, response.data)

