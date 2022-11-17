from django.test import TestCase, Client
from django.urls import reverse
from my_market.models import Store, Product


class TestViews(TestCase):
    def test_redirect_to_login_GET(self):
        client = Client()
        response = client.get(reverse("home"))
        self.assertEquals(response.status_code, 302)
