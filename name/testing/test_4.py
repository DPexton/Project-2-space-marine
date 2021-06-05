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
       'Space Wolves,Terminator Marine': b"Tyreous Hengun",
       'Ultramarines,Tactical Marine': b"Titus Grimaldus",
       'Ultramarines,Assault Marine': b"Maximus Tarimus",
       'Ultramarines,Devastator Marine': b"Jonah Sidonis",
       'Ultramarines,Scout Marine': b"Barachiel Sadros",
       'Ultramarines,Terminator Marine': b"Aecon Evidist",
       'Imperial Fists,Tactical Marine': b"Shal Cestros",
       'Imperial Fists,Assault Marine': b"Uziel Aryabhon",
       'Imperial Fists,Devastator Marine': b"Klordath Aglibesco",
       'Imperial Fists,Scout Marine': b"Kazryn Batariar",
       'Imperial Fists,Terminator Marine': b"Kazrago Hannibia",
       'Dark Angels,Tactical Marine': b"Baelar Sadross",
       'Dark Angels,Assault Marine': b"Gabriel Manuzanus",
       'Dark Angels,Devastator Marine': b"Lutheon Alcane",
       'Dark Angels,Scout Marine': b"Cassias Gabrun",
       'Dark Angels,Terminator Marine': b"Anaticus Redlici",
       'Salamanders,Tactical Marine': b"Belial Iasiar",
       'Salamanders,Assault Marine': b"Varreon Baaloss",
       'Salamanders,Devastator Marine': b"Sappheran Petrail",
       'Salamanders,Scout Marine': b"Ophaniel Salatis",
       'Salamanders,Terminator Marine': b"Maximiz Zephit",
       'Blood Angels,Tactical Marine': b"Beler Antilochiad",
       'Blood Angels,Assault Marine': b"Azazel Annellurius",
       'Blood Angels,Devastator Marine': b"Ubaldun Chronal",
       'Blood Angels,Scout Marine': b"Azreal Berian",
       'Blood Angels,Terminator Marine': b"Sarathiel Asbeo"
    }
    def test_spacewolves1(self):
        for data,result in self.test_cases.items():
            response = self.client.post(
                url_for('name'),
                data = data
                )
            self.assertIn(result, response.data)

