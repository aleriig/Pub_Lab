import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    

    def setUp(self): # NEW
        self.customer = Customer("Andrew", 50.00) # NEW

    def test_customer_has_name_and_wallet(self): # NEW
        self.assertEqual("Andrew", self.customer.name)
        
    def test_customer_can_reduce_wallet(self):
        self.customer.reduce_wallet(3.5)
        self.assertEqual(46.50, self.customer.wallet)    
        
    
    