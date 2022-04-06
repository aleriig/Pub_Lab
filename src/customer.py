from operator import truediv


class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.consumed_drinks = []
        self.consumed_units = 0

    def reduce_wallet(self, wallet_reduction):
        self.wallet -= wallet_reduction    
    
    def consume_drink(self, drink):
        self.consumed_drinks.append(drink)
        self.consumed_units += drink.units
        self.wallet -= drink.price

    def is_pished(self):
        total_units = 0

        for drink in self.consumed_drinks:
            total_units += drink.units

        if total_units >= 8:
            return True
        else: 
            return False
