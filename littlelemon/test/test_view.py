from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        self.client = Client()
        Menu.objects.create(Title = "Karahi", Price = 2.50, Inventory = 45)
        Menu.objects.create(Title = "Nihari", Price = 4.50, Inventory = 40)

    def test_getall(self):
        response = self.client.get(reverse('menu'))
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)
        