import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    pass

    def setUp(self): # NEW
        self.customer = Customer("Harry", 100) # NEW

    def test_customer_has_name(self): # NEW
        self.assertEqual("Harry", self.customer.name) # NEW