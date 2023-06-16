from django.test import TestCase
from .models import Product
# Create your tests here.

class ModelTesting(TestCase):
    def setUp(self) -> None:
        self.product_get = Product.objects.filter(id="7e4ff4f4cab7484fafcd4e6022b45341")


    def test_get_product(self):
        d = self.product_get
        self.assertTrue(isinstance(d, Product))
