from urllib import response
from django.test import TestCase
from django.test import Client

# Create your tests here.
class Testing(TestCase):
    def test_the_html(self):
        response = self.client.get(('/mywatchlist/html/'))
        self.assertEquals(response.status_code, 200)

    def test_the_json(self):
        response = self.client.get(('/mywatchlist/json/'))
        self.assertEquals(response.status_code, 200)

    def test_the_xml(self):
        response = self.client.get(('/mywatchlist/xml/'))
        self.assertEquals(response.status_code, 200)
