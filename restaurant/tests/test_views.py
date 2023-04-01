from django.test import TestCase
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pho", price=20, inventory=1000)

    def test_getall(self):
        menus = Menu.objects.all()
        self.assertEqual(len(menus), 2)
