from class_Restaurant import Restaurant
from class_Restaurant import IceCreamStand
import unittest

class TestRestaurant(unittest.TestCase):

    def setUp(self):
        self.new_restaurant = Restaurant('Lotus','Chinese')

    def test_open_restaurant(self):
        opened = self.new_restaurant.open_restaurant()
        #print opened
        self.assertEqual(opened, "Come in, Lotus is opened!")

    def test_number_served(self):
        total_served = self.new_restaurant.number_served(200)
        self.assertEqual(self.new_restaurant.customers_served,200)
        self.assertEqual(total_served, "The number of customers served at Lotus is 200.")
#unittest.main()

class TestIceCreamStand(unittest.TestCase):

    def setUp(self):
        self.ice_cream_shop = IceCreamStand()
        self.ice_cream_flavors = ['Chocolate','Vanilla','Straberry','Pecan']

    def test_flavors(self):
        for flavor in self.ice_cream_flavors:
            self.ice_cream_shop.flavors.append(flavor)
        for flavor in self.ice_cream_flavors:
            self.assertIn(flavor,self.ice_cream_shop.flavors)
unittest.main()       
