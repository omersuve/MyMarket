from django.test import SimpleTestCase
from django.urls import reverse, resolve
from my_market.views import *


class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func, index)

    def test_add_store_user_url_is_resolved(self):
        url = reverse("add_store_user", args=[1])
        self.assertEquals(resolve(url).func, add_store_user)

    def test_remove_product_user_url_is_resolved(self):
        url = reverse("remove_product_user", args=[1])
        self.assertEquals(resolve(url).func, remove_product_user)

    def test_remove_store_user_url_is_resolved(self):
        url = reverse("remove_store_user", args=[1])
        self.assertEquals(resolve(url).func, remove_store_user)

    def test_product_details_url_is_resolved(self):
        url = reverse("product_details", args=["some-arg"])
        self.assertEquals(resolve(url).func, product_details)

    def test_products_by_store_url_is_resolved(self):
        url = reverse("store_details", args=["some-arg"])
        self.assertEquals(resolve(url).func, products_by_store)

    def test_add_product_url_is_resolved(self):
        url = reverse("add_product", args=["some-arg"])
        self.assertEquals(resolve(url).func, add_product)

    def test_remove_product_url_is_resolved(self):
        url = reverse("remove_product", args=["some-arg", "some-arg"])
        self.assertEquals(resolve(url).func, remove_product)
