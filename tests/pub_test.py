# tests/pub_test.py

import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    

    def setUp(self): # NEW
        self.pub = Pub("The Chanter", 100.00)
        self.drink_1 = Drink("Beer", 2, 3.50)
        self.drink_2 = Drink("Wine", 3, 5.00)
        self.drink_3 = Drink("Vodka", 5,  6.40)
        self.customer = Customer("Andrew", 50.00)

    def test_pub_has_name(self): # NEW
        self.assertEqual("The Chanter", self.pub.name) # NEW  

    def test_pub_has_a_till(self):
        self.assertEqual(100.00, self.pub.till) 

    def test_pub_has_drinks(self):
        self.assertEqual(0,len(self.pub.drinks))       

    def test_add_drinks(self):
        self.pub.add_drink_to_pub(self.drink_1)
        self.pub.add_drink_to_pub(self.drink_2)
        self.pub.add_drink_to_pub(self.drink_3)
        self.assertEqual(3,len(self.pub.drinks)) 

    
    def test_has_drunk_customer(self):
        self.customer.consume_drink(self.drink_1)
        self.customer.consume_drink(self.drink_1)
        self.customer.consume_drink(self.drink_1)
        self.customer.consume_drink(self.drink_1)
        self.customer.consume_drink(self.drink_1)
        self.assertEqual(True, self.customer.is_pished())
        self.assertEqual(10, self.customer.consumed_units)


    def test_empty_wallet(self):
        self.customer.consume_drink(self.drink_1)
        self.customer.consume_drink(self.drink_1)
        self.assertEqual(43, self.customer.wallet)
    
    
    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till) # NEW        
              

    

