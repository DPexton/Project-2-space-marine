from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_spacewolves1(self):
        with patch('requests.get') as i:
            i.return_value.text = "Space Wolves"
            with patch('random.randrange') as r:
                r.return_value = "Tactical Marine"
                response = self.client.post(
                    url_for('name'),
                    data = 'Tactical Marine Space Wolves'
                )
                self.assertIn(b"Grimolf Ulfsson", response.data)

class TestResponse(TestBase):
    def test_spacewolves2(self):
        with patch('requests.get') as i:
            i.return_value.text = "Space Wolves"
            with patch('random.randrange') as r:
                r.return_value = "Assault Marine"
                response = self.client.post(
                    url_for('name'),
                    data = 'Assault Marine Space Wolves'
                )
                self.assertIn(b"Ragnar Blackmane", response.data)

class TestResponse(TestBase):
    def test_spacewolves3(self):
        with patch('requests.get') as i:
            i.return_value.text = "Space Wolves"
            with patch('random.randrange') as r:
                r.return_value = "Devastator Marine"
                response = self.client.post(
                    url_for('name'),
                    data = 'Devastator Marine Space Wolves'
                )
                self.assertIn(b"Gunbjorn Ironmaw", response.data)

class TestResponse(TestBase):
    def test_spacewolves4(self):
        with patch('requests.get') as i:
            i.return_value.text = "Space Wolves"
            with patch('random.randrange') as r:
                r.return_value = "Scout Marine"
                response = self.client.post(
                    url_for('name'),
                    data = 'Scout Marine Space Wolves'
                )
                self.assertIn(b"One-Eye Frodi", response.data)

class TestResponse(TestBase):
    def test_ultramarines1(self):
        with patch('requests.get') as i:
            i.return_value.text = "Ultramarines"
            with patch('random.randrange') as r:
                r.return_value = "Tactical Marine"
                response = self.client.post(
                    url_for('name'),
                    data = 'Tactical Marine Ultramarines'
                )
                self.assertIn(b"Titus Grimaldus", response.data)

class TestResponse(TestBase):
    def test_ultramarines2(self):
        with patch('requests.get') as i:
            i.return_value.text = "Ultramarines"
            with patch('random.randrange') as r:
                r.return_value = "Assault Marine"
                response = self.client.post(
                    url_for('name'),
                    data = 'Assault Marine Ultramarines'
                )
                self.assertIn(b"Maximus Tarimus", response.data)

class TestResponse(TestBase):
    def test_ultramarines3(self):
        with patch('requests.get') as i:
            i.return_value.text = "Ultramarines"
            with patch('random.randrange') as r:
                r.return_value = "Devastator Marine"
                response = self.client.post(
                    url_for('name'),
                    data = 'Devastator Marine Ultramarines'
                )
                self.assertIn(b"Jonah Sidonis", response.data)

class TestResponse(TestBase):
    def test_ultramarines4(self):
        with patch('requests.get') as i:
            i.return_value.text = "Ultramarines"
            with patch('random.randrange') as r:
                r.return_value = "Scout Marine"
                response = self.client.post(
                    url_for('name'),
                    data = 'Scout Marine Ultramarines'
                )
                self.assertIn(b"Barachiel Sadros", response.data)

class TestResponse(TestBase):
    def test_imperialfists1(self):
        with patch('requests.get') as i:
            i.return_value.text = "Imperial Fists"
            with patch('random.randrange') as r:
                r.return_value = "Tactical Marine"
                response = self.client.post(
                    url_for('name'),
                    data = 'Tactical Marine Imperial Fists'
                )
                self.assertIn(b"Shal Cestros", response.data)

class TestResponse(TestBase):
    def test_imperialfists2(self):
        with patch('requests.get') as i:
            i.return_value.text = "Imperial Fists"
            with patch('random.randrange') as r:
                r.return_value = "Assault Marine"
                response = self.client.post(
                    url_for('name'),
                    data = 'Assault Marine Imperial Fists'
                )
                self.assertIn(b"Uziel Aryabhon", response.data)

class TestResponse(TestBase):
    def test_imperialfists3(self):
        with patch('requests.get') as i:
            i.return_value.text = "Imperial Fists"
            with patch('random.randrange') as r:
                r.return_value = "Devastator Marine"
                response = self.client.post(
                    url_for('name'),
                    data = 'Devastator Marine Imperial Fists'
                )
                self.assertIn(b"Klordath Aglibesco", response.data)

class TestResponse(TestBase):
    def test_imperialfists4(self):
        with patch('requests.get') as i:
            i.return_value.text = "Imperial Fists"
            with patch('random.randrange') as r:
                r.return_value = "Scout Marine"
                response = self.client.post(
                    url_for('name'),
                    data = 'Scout Marine Imperial Fists'
                )
                self.assertIn(b"Kazryn Batariar", response.data)

class TestResponse(TestBase):
    def test_darkangels1(self):
        with patch('requests.get') as i:
            i.return_value.text = "Dark Angels"
            with patch('random.randrange') as r:
                r.return_value = "Tactical Marine"
                response = self.client.post(
                    url_for('name'),
                    data = 'Tactical Marine Dark Angels'
                )
                self.assertIn(b"Baelar Sadross", response.data)

class TestResponse(TestBase):
    def test_darkangels2(self):
        with patch('requests.get') as i:
            i.return_value.text = "Dark Angels"
            with patch('random.randrange') as r:
                r.return_value = "Assault Marine"
                response = self.client.post(
                    url_for('name'),
                    data = 'Assault Marine Dark Angels'
                )
                self.assertIn(b"Gabriel Manuzanus", response.data)

class TestResponse(TestBase):
    def test_darkangels3(self):
        with patch('requests.get') as i:
            i.return_value.text = "IDark Angels"
            with patch('random.randrange') as r:
                r.return_value = "Devastator Marine"
                response = self.client.post(
                    url_for('name'),
                    data = 'Devastator Marine Dark Angels'
                )
                self.assertIn(b"Lutheon Alcane", response.data)

class TestResponse(TestBase):
    def test_darkangels4(self):
        with patch('requests.get') as i:
            i.return_value.text = "Dark Angels"
            with patch('random.randrange') as r:
                r.return_value = "Scout Marine"
                response = self.client.post(
                    url_for('name'),
                    data = 'Scout Marine Dark Angels'
                )
                self.assertIn(b"Cassias Gabrun", response.data)