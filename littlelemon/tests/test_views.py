from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu  # Import your Menu model
import json


class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(ID=3, Title="Test Menu 1", Price=10.99, Inventory=100)
        Menu.objects.create(ID=4, Title="Test Menu 2", Price=15.99, Inventory=100)

    def test_getall(self):
        # Retrieve all Menu objects
        response = self.client.get(
            reverse("menu-list")
        )  # Assuming 'menu-list' is the URL name for your view
        menus = Menu.objects.all()
        serialized_data = [
            {
                "ID": menu.ID,
                "Title": menu.Title,
                "Price": str(menu.Price),
                "Inventory": menu.Inventory,
            }
            for menu in menus
        ]
        # Check if the response data matches the serialized data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized_data)
