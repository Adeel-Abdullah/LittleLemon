from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_Menu_string(self):
        item = Menu.objects.create(Title="IceCream", Price = 1.5, Inventory = 30)
        self.assertEqual(str(item), "IceCream : 1.5")