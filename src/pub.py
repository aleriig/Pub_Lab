class Pub:

    def __init__(self, name, till):
        self.name = name 
        self.till = till
        self.drinks = []

    def add_drink_to_pub(self, drink):
        self.drinks.append(drink)
        
    
    def increase_till(self, amount):
        self.till += amount