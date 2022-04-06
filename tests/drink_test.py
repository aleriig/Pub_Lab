import unittest
from src.drink import Drink
from src.customer import Customer

class TestDrinks(unittest.TestCase):
    

    def setUp(self): # NEW
        self.drink = Drink("Beer", 2, 3.50) # NEW

    def test_drinks_has_name(self): # NEW
        self.assertEqual("Beer", self.drink.name) # NEW 

    def test_drinks_has_a_price(self):
        self.assertEqual(3.50, self.drink.price)
     